# Google Search CSV Export Tool

A Python-based app using Flask that allows you to retrieve Google search results for a domain and export them to a CSV file.

## Setup

1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Package installation

```bash
pip install -r requirements.txt
```

3. Set up Google API credentials
Create a .env file in the project root or set environment variables in your system:

```bash
GOOGLE_API_KEY=YOUR_API_KEY
GOOGLE_CSE_ID=YOUR_CSE_ID
```

4. Run the Flask application
```bash
python app.py
```