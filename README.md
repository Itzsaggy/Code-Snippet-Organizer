# Code Snippet Organizer with AI Tags

A web application built with Python and Flask that lets you save, organize, and tag code snippets intelligently. Powered by spaCy for AI-driven tagging, it features a modern UI, real-time search, tag editing, individual snippet deletion, and syntax highlighting—all deployed live on Render.



## Features![Screenshot (969)](https://github.com/user-attachments/assets/b0f1b47b-6ab7-43a4-9b82-4116322b3a88)

- **AI Tagging**: Automatically tags snippets (e.g., "function," "loop," "web") using spaCy NLP and keyword matching.
- **Persistent Storage**: Saves snippets to a JSON file for durability.
- **Real-Time Search**: Filter snippets by code or tags instantly.
- **Tag Editing**: Manually tweak tags per snippet.
- **Delete Snippets**: Remove individual snippets with a button.
- **Syntax Highlighting**: Displays code with colorful formatting via `highlight.js`.
- **Aesthetic Design**: Dark-mode UI with neon accents and smooth animations.
- **Live Deployment**: Hosted on Render for public access.

## Live Demo
Try it out at: [https://code-snippet-org-123.onrender.com](https://code-snippet-org-123.onrender.com)  


## Tech Stack
- **Backend**: Python, Flask
- **AI/NLP**: spaCy (`en_core_web_sm` model)
- **Frontend**: HTML, CSS, JavaScript
- **Syntax Highlighting**: `highlight.js`
- **Deployment**: Render
- **Storage**: JSON file

## Installation (Local Setup)
1. Clone the Repo:
   git clone https://github.com/yourusername/code-snippet-organizer.git
   cd code-snippet-organizer

2. Install Dependencies:
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

3. Run the App:
   python app.py
