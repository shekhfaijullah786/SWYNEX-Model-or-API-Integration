# SWYNEX – AI Study Notes Summarizer

A small AI prototype built for SWYNEX Task 2 (Model or API Integration).

## Overview

The AI Study Notes Summarizer accepts text notes and uses Google's Gemini API
to produce:
- A summary
- Important key points
- Five revision questions with short answers

The interface is built with Streamlit and the model is accessed through
Google's official `google-genai` Python SDK.

## Tech stack

- Python
- Streamlit
- Google Gemini API
- `google-genai`
- `python-dotenv`

## Project structure

```text
SWYNEX-Model-or-API-Integration/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

1. Install Python 3.10 or later.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file by copying `.env.example`.
7. Add your Gemini API key to `.env`:

   ```text
   GEMINI_API_KEY=your_key_here
   ```

   Keep this key private. Do not commit `.env` or paste the key into screenshots,
   public posts, or source code. Check the API provider's current age, account,
   usage, and billing requirements with a parent/guardian if needed. Do not enable
   paid billing for this student prototype.

8. Start the app:

   ```bash
   streamlit run app.py
   ```

The app will open in your browser.

## Example input

```text
Photosynthesis is the process by which green plants use sunlight to make food.
Chlorophyll in the leaves absorbs light energy. Plants take in carbon dioxide
from the air and water from the soil. Glucose is produced and oxygen is released.
```

## Example output (illustrative)

**Summary:** Photosynthesis is how green plants use sunlight to make glucose
from water and carbon dioxide. Chlorophyll captures light energy, and oxygen
is released during the process.

**Key points:**
- Photosynthesis occurs in green plants.
- Chlorophyll absorbs light energy.
- Water and carbon dioxide are used.
- Glucose is produced and oxygen is released.

**Revision question:** What does chlorophyll do?

**Answer:** It absorbs light energy.

Note: This is an illustrative example, not a recorded response from the live API.

## How it works

1. The user pastes notes into the Streamlit text area.
2. The app builds a prompt with the selected detail level.
3. The Google GenAI SDK sends the prompt to the Gemini model.
4. The app displays the generated study guide.

## Limitations

- An internet connection and a valid API key are required.
- Model responses can contain errors; verify important information with
  trusted course materials.
- Very long notes may exceed model or service limits.

## Security

Never publish API keys. Store the key in `.env`, which is excluded by `.gitignore`.
If a key is accidentally exposed, revoke it and create a replacement.

## Task 2 submission checklist

- [ ] Run the app and test it with sample notes.
- [ ] Capture a screenshot showing the input and generated result.
- [ ] Push this project to a GitHub repository named
      `SWYNEX-Model-or-API-Integration`.
- [ ] Publish a short LinkedIn explanation with a screenshot or demo.
- [ ] Submit the GitHub URL and LinkedIn post URL on the SWYNEX dashboard.
