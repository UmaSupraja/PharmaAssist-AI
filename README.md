# PharmaAssist AI


PharmaAssist AI is a healthcare information website and rule-based NLP chatbot built with Python, Flask, HTML, CSS and JavaScript. It helps users find medical stores in Visakhapatnam, access emergency helplines, understand prescription support and learn everyday health tips.

### [View the live PharmaAssist AI website](https://pharmaassistai.onrender.com/)

## Problem and Solution

**Problem:** Users need a simple way to find nearby pharmacies, emergency helplines, prescription guidance and basic health tips in one place.

**Solution:** PharmaAssist AI provides a single responsive website with pharmacy information, emergency contacts, health tips and a rule-based chatbot. It does not require login, payment or an external AI API.

## Features

- Pharmacy directory for Visakhapatnam
- 24-hour and late-night pharmacy filters
- Emergency helpline numbers: 108, 112 and 104
- First-aid and health-tip information
- Prescription file preview without uploading
- Rule-based chatbot for common health questions
- Voice input support using the browser Web Speech API
- Responsive design for mobile and desktop
- Public deployment on Render

## Modules

| Module | Description |
|---|---|
| Pharmacy Directory | Displays medical stores with address, timing, phone number and map link |
| Medicine Categories | Shows common medicine and wellness product groups |
| Prescription Support | Allows users to select and preview a JPG, PNG or PDF file locally |
| Emergency Help | Provides ambulance, emergency and health helpline numbers |
| Health Tips | Provides hydration, nutrition, fitness, sleep and prevention tips |
| Chatbot | Answers predefined questions using keyword matching |

## Chatbot Workflow

```text
User Question
      │
      ▼
JavaScript sends message
      │
      ▼
Flask /chat API
      │
      ▼
Convert text to lowercase
      │
      ▼
Split into words and remove punctuation
      │
      ▼
Compare with KNOWLEDGE_BASE keywords
      │
      ▼
Select highest-scoring answer
      │
      ▼
Return response to chatbot UI
```

## How the Chatbot Works

1. The user opens the PharmaAssist AI chatbot and types a question.
2. JavaScript sends the user question to the Flask `/chat` API.
3. Flask receives the question and converts it to lowercase.
4. Flask splits the question into individual words.
5. Punctuation is removed from the beginning and end of each word.
6. The cleaned words are compared with keywords stored in `KNOWLEDGE_BASE`.
7. Each matching keyword receives a score; multi-word phrases receive a higher score.
8. Flask selects the answer with the highest matching score.
9. Flask returns the selected answer to JavaScript in JSON format.
10. JavaScript displays the chatbot response in the chat window.

## Technologies Used

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Chatbot | Rule-based keyword matching |
| Database | No database is used |
| Production server | Gunicorn |
| Deployment | Render |
| Version control | Git and GitHub |


## Project Structure

```text
PharmaAssist_AI_Python/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Installation

Clone the repository:

```bash
git clone [https://github.com/UmaSupraja/PharmaAssist-AI.git](https://github.com/UmaSupraja/PharmaAssist-AI.git)
cd PharmaAssist-AI
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Flask application:

```bash
python app.py
```

Open the website in your browser:

```text
http://127.0.0.1:5000
```

## Deployment

The project is deployed on Render.

- **Live website:** https://pharmaassistai.onrender.com/
- **GitHub repository:** https://github.com/UmaSupraja/PharmaAssist-AI
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

## Author

**Supraja Putrevu**  
B.Tech – Computer Science & Engineering (Data Science)  
Python Developer | AI Enthusiast | Data Science | Machine Learning  

GitHub: [https://github.com/UmaSupraja](https://github.com/UmaSupraja)
