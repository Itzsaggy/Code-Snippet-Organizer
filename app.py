from flask import Flask, render_template, request, redirect, url_for
import spacy
import json
import os

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
SNIPPETS_FILE = "snippets.json"

def load_snippets():
    if os.path.exists(SNIPPETS_FILE):
        with open(SNIPPETS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_snippets(snippets):
    with open(SNIPPETS_FILE, 'w') as f:
        json.dump(snippets, f, indent=4)

snippets = load_snippets()

def tag_snippet(code):
    doc = nlp(code)
    tags = []
    keywords = {
        "sort": ["sort", "sorted", "sorting", "quicksort"],
        "loop": ["for", "while", "loop"],
        "web": ["http", "url", "flask", "request", "response"],
        "function": ["def", "function", "lambda"],
        "print": ["print"],
        "data": ["list", "dict", "array", "set"],
        "condition": ["if", "else", "elif"],
    }
    code_lower = code.lower()
    for tag, words in keywords.items():
        if any(word in code_lower for word in words):
            tags.append(tag)
    return tags if tags else ["general"]

@app.route('/', methods=['GET', 'POST'])
def home():
    filtered_snippets = snippets
    search_query = ""

    if request.method == 'POST':
        snippet = request.form.get('snippet')
        if snippet:
            tags = tag_snippet(snippet)
            snippets.append({"code": snippet, "tags": tags})
            save_snippets(snippets)
            return redirect(url_for('home'))

    search_query = request.args.get('search', '').lower()
    if search_query:
        filtered_snippets = [
            s for s in snippets
            if search_query in s["code"].lower() or any(search_query in tag.lower() for tag in s["tags"])
        ]

    return render_template('index.html', snippets=filtered_snippets, search_query=search_query)

@app.route('/clear')
def clear():
    snippets.clear()
    save_snippets(snippets)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(snippets):
        snippets.pop(index)
        save_snippets(snippets)
    return redirect(url_for('home'))

@app.route('/edit_tags/<int:index>', methods=['POST'])
def edit_tags(index):
    if 0 <= index < len(snippets):
        new_tags = request.form.get('tags').split(',')
        snippets[index]["tags"] = [tag.strip() for tag in new_tags if tag.strip()]
        save_snippets(snippets)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)