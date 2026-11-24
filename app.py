# PharmaAssist AI - simple keyword chatbot using Flask
# No AI model, no database. Answers come from the list below.

import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# ---------------------------------------------------------
# KNOWLEDGE BASE
# Each topic has:  keywords (words a user may type)  and  an answer.
# To teach the chatbot something new, add one more topic here.
# ---------------------------------------------------------
topics = [
    {
        "keywords": ["late night", "until late", "night pharmacy", "night medical store",
                     "midnight", "11 pm", "11pm", "12 am", "suraksha medicals",
                     "mohan medical shop", "aganampudi"],
        "answer": "Late-night pharmacies in Vizag include Suraksha Medicals (KGH Down Road), "
                  "Mohan Medical Shop (ZP Branch) and Apollo Pharmacy (Aganampudi). "
                  "Call first to confirm timings and medicine availability."
    },
    {
        "keywords": ["24/7", "24 hour", "24 hours", "twenty four", "open now", "open pharmacy",
                     "open medical store", "medical store open", "pharmacy open",
                     "24-hour", "all night"],
        "answer": "Some pharmacies listed as 24-hour in Vizag are Sainadh Medicals, "
                  "Apollo Pharmacy (Siripuram), Subham Chemists Medizone and Health Care Pharmacy. "
                  "Please call first to confirm they are open and have your medicine."
    },
    {
        "keywords": ["pharmacy", "medical store", "chemist", "medical shop",
                     "store address", "store location", "pharmacy location"],
        "answer": "Check the Medical Stores section for pharmacy addresses, timings and phone numbers. "
                  "Call the pharmacy to confirm the latest details."
    },
    {
        "keywords": ["home delivery", "door delivery", "delivery", "deliver medicine",
                     "online order", "order medicine", "medicine delivery"],
        "answer": "PharmaAssist does not arrange medicine delivery. Call a nearby pharmacy to ask "
                  "whether it delivers to your area and whether your medicine is available."
    },
    {
        "keywords": ["available", "availability", "in stock", "stock", "check medicine",
                     "have this medicine", "medicine price", "price of medicine"],
        "answer": "I cannot check live medicine stock or prices. Call a pharmacy with the medicine's "
                  "name, strength and quantity; keep a prescription ready if required."
    },
    {
        "keywords": ["emergency number", "emergency numbers", "ambulance", "108", "112", "104",
                     "emergency contact", "medical emergency", "urgent help", "helpline"],
        "answer": "For any emergency in India, call 112. For an ambulance or medical emergency, "
                  "call 108; for health advice and support, call 104. If someone is seriously unwell, "
                  "injured, or in immediate danger, call 112 or 108 now."
    },
    {
        "keywords": ["health tips", "healthy habits", "stay healthy", "wellness",
                     "healthy lifestyle", "good health", "health advice"],
        "answer": "Eat a variety of healthy foods, drink enough water, stay physically active, "
                  "and get regular sleep. Avoid tobacco, limit excess salt and sugar, and see a "
                  "healthcare professional for regular check-ups."
    },
    {
        "keywords": ["hospital", "nearby hospital", "nearest hospital", "kgh", "king george",
                     "apollo hospital", "sevenhills", "seven hills", "health city"],
        "answer": "Major Vizag hospitals include King George Hospital (KGH), Apollo Hospitals "
                  "(Health City) and SevenHills Hospital. For emergencies, call 108 or 112."
    },
    {
        "keywords": ["prescription", "upload prescription", "upload", "jpg", "png", "pdf",
                     "prescription photo", "prescription file"],
        "answer": "Choose a JPG, PNG or PDF prescription (up to 10 MB), then select \"Review selected file\". "
                  "This demo only previews the file in your browser; it does not send it anywhere."
    },
    {
        "keywords": ["refill", "repeat medicine", "repeat prescription", "renew prescription",
                     "refill request", "monthly medicines"],
        "answer": "For a refill, contact your pharmacy with your latest prescription and medicine details. "
                  "Do not change or stop regular medicines without your doctor's advice."
    },
    {
        "keywords": ["paracetamol", "dolo 650", "crocin", "ibuprofen", "fever medicine",
                     "painkiller", "pain relief", "fever", "headache"],
        "answer": "Paracetamol is commonly used for fever and pain; ibuprofen can help with pain and swelling. "
                  "Follow the label or your doctor's advice, and ask a pharmacist if unsure."
    },
    {
        "keywords": ["cetirizine", "cold", "cough", "allergy", "sneezing", "runny nose",
                     "cough syrup", "lozenges", "nasal spray", "sore throat"],
        "answer": "Cold, cough and allergy products include cetirizine, cough syrups and nasal sprays. "
                  "Ask a pharmacist which option is suitable, especially for children or during pregnancy."
    },
    {
        "keywords": ["diabetes", "blood sugar", "insulin", "blood pressure", "hypertension",
                     "bp medicine", "thyroid", "heart care"],
        "answer": "Take diabetes, BP, thyroid and heart medicines exactly as prescribed. "
                  "Do not start, stop or change a dose without speaking to your doctor."
    },
    {
        "keywords": ["vitamin", "multivitamin", "calcium", "vitamin d", "protein powder",
                     "supplement", "nutrition supplement"],
        "answer": "Common supplements include multivitamins, calcium, vitamin D and protein powder. "
                  "Ask a healthcare professional before taking them regularly or in high doses."
    },
    {
        "keywords": ["thermometer", "bp monitor", "blood pressure monitor", "pulse oximeter",
                     "oximeter", "glucometer", "medical device"],
        "answer": "Common home devices include thermometers, BP monitors, pulse oximeters and glucometers. "
                  "Follow the instructions and ask a healthcare professional how to understand the readings."
    },
    {
        "keywords": ["first aid", "bleeding", "burn", "burns", "cut", "wound", "bandage",
                     "antiseptic", "cotton", "medical tape", "choking", "unconscious"],
        "answer": "For heavy bleeding, apply firm pressure and call emergency services; cool minor burns "
                  "under running water for 20 minutes. For serious injuries, call 108/112 and get medical help."
    },
    {
        "keywords": ["water", "hydration", "drink water", "dehydration", "how much water", "thirst"],
        "answer": "Drink water regularly, and have extra fluids during hot weather or exercise. "
                  "If you have a health condition that limits fluids, follow your doctor's advice."
    },
    {
        "keywords": ["nutrition", "diet", "healthy food", "balanced diet", "eat healthy", "meal"],
        "answer": "Eat a balanced diet with fruits, vegetables, whole grains, pulses and protein. "
                  "Try to limit excess salt, sugar and highly processed foods."
    },
    {
        "keywords": ["fitness", "exercise", "walking", "workout", "physical activity", "activity"],
        "answer": "Try walking, cycling, stretching or other activities you enjoy. Start slowly, "
                  "and ask your doctor before major changes if you have a health condition."
    },
    {
        "keywords": ["sleep", "insomnia", "sleep routine", "sleep tips", "cannot sleep", "cant sleep"],
        "answer": "For better sleep, keep a regular bedtime, reduce screen use before bed and avoid "
                  "caffeine late in the day. See a healthcare professional if sleep problems continue."
    },
    {
        "keywords": ["preventive", "prevention", "health checkup", "check up", "vaccination",
                     "vaccine", "health awareness", "screening"],
        "answer": "Stay healthy with recommended vaccines, regular check-ups, good hygiene, safe food "
                  "and water, physical activity and by avoiding tobacco. Ask your doctor which checks you need."
    },
    {
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "namaste"],
        "answer": "Hello! I'm PharmaAssist. Ask me about Vizag pharmacies, medicines, prescriptions, "
                  "emergency numbers, hospitals, first aid or healthy habits."
    },
    {
        "keywords": ["help", "what can you do", "topics", "features", "how can you help", "options"],
        "answer": "I can help with common questions about pharmacies, medicines, delivery, refills, "
                  "prescriptions, emergencies, hospitals, first aid and healthy habits."
    },
]

NOT_FOUND_ANSWER = (
    "I don't have a predefined answer for that question yet. I can help "
    "with pharmacies in Vizag, medicine categories, prescription uploads, "
    "refill guidance, emergency contacts, hospitals, first aid and general "
    "wellness. For diagnosis or treatment advice, contact a qualified "
    "healthcare professional."
)


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------
def get_words(text):
    """Turn a sentence into a list of clean lowercase words.
    Example: "Any 24 hour pharmacy?"  ->  ["any", "24", "hour", "pharmacy"]
    """
    clean_words = []
    for word in text.lower().split():
        word = word.strip(".,!?;:'\"()[]{}")   # remove punctuation at both ends
        if word != "":
            clean_words.append(word)
    return clean_words


def find_answer(user_message):
    """Find the topic whose keywords match the user's message best."""
    user_words = get_words(user_message)

    if len(user_words) == 0:
        return "Please type a question so I can help."

    best_answer = NOT_FOUND_ANSWER
    best_score = 0

    for topic in topics:
        score = 0

        for keyword in topic["keywords"]:
            keyword_words = get_words(keyword)

            if len(keyword_words) == 0:
                continue

            # Check that every word of the keyword is in the user's message.
            all_found = True
            for word in keyword_words:
                if word not in user_words:
                    all_found = False

            if all_found:
                if len(keyword_words) > 1:
                    score = score + 4 + len(keyword_words)   # phrases count more
                else:
                    score = score + 1

        if score > best_score:
            best_score = score
            best_answer = topic["answer"]

    return best_answer


# ---------------------------------------------------------
# WEB PAGES
# ---------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if data is None:
        data = {}

    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"response": "Please enter your question as text."}), 400

    return jsonify({"response": find_answer(message)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
