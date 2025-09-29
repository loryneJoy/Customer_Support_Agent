
    """Simple Customer Support Chatbot
    - CLI interactive mode
    - also contains a small Flask API (optional) if you want to run a local server
    """
    from collections import Counter
    import re
    import sys

    CATEGORIES = {
        "Billing": {
            "keywords": ["payment", "invoice", "bill", "charge", "refund", "subscription", "card", "billing"],
            "response": "For billing questions, please check your account settings or contact billing support at billing@example.com."
        },
        "Technical Support": {
            "keywords": ["error", "problem", "not working", "issue", "bug", "crash", "slow", "connect", "disconnect"],
            "response": "Please try restarting your device. If the problem persists, contact technical support at techsupport@example.com."
        },
        "General Inquiry": {
            "keywords": ["hours", "location", "contact", "where", "when", "open", "business hours", "address"],
            "response": "Our business hours are 9 AM to 5 PM, Monday to Friday. You can contact us at info@example.com."
        }
    }

    ESCALATION_KEYWORDS = {"angry", "frustrated", "not happy", "upset", "furious", "annoyed", "disappointed"}

    def normalize(text):
        return text.lower()

    def classify_question(text):
        text_l = normalize(text)
        # Count matches per category (match whole words or keyword phrases)
        counts = Counter()
        for cat, info in CATEGORIES.items():
            for kw in info['keywords']:
                # simple phrase or word match
                pattern = r'\b' + re.escape(kw.lower()) + r'\b'
                matches = re.findall(pattern, text_l)
                if matches:
                    counts[cat] += len(matches)
        if not counts:
            return "Unknown", None, False
        # choose the category with highest count
        top_cat, top_count = counts.most_common(1)[0]
        return top_cat, CATEGORIES[top_cat]['response'], (top_count > 0)

    def detect_escalation(text):
        text_l = normalize(text)
        for kw in ESCALATION_KEYWORDS:
            if re.search(r'\b' + re.escape(kw) + r'\b', text_l):
                return True
        return False

    def chat_once(user_input):
        cat, response, matched = classify_question(user_input)
        escalate = detect_escalation(user_input)
        if escalate:
            escalation_msg = "I understand this is frustrating. Let me connect you with a human representative."
        else:
            escalation_msg = None
        if cat == "Unknown":
            reply = "I'm sorry — I didn't quite understand. Could you please clarify or try different words?"
        else:
            reply = response
        # If escalation suggested, prepend empathy
        if escalation_msg:
            reply = escalation_msg + " " + reply
        return {"category": cat, "response": reply, "escalate": escalate}


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--api':
        # Lazy import so Flask is optional
        try:
            from flask import Flask, request, jsonify
        except Exception as e:
            print('Flask is required to run the API. Install with: pip install flask')
            sys.exit(1)
        app = Flask(__name__)

        @app.route('/api/classify', methods=['POST'])
        def api_classify():
            data = request.get_json(force=True)
            q = data.get('question','')
            result = chat_once(q)
            return jsonify(result)

        print('Starting API on http://127.0.0.1:5000')
        app.run(debug=True)
    else:
        print('Simple Customer Support Chatbot (type "exit" to quit)')
        while True:
            try:
                user = input('You: ').strip()
            except EOFError:
                break
            if not user or user.lower() in ('exit','quit'):
                print('Goodbye!')
                break
            out = chat_once(user)
            print('\nBot:')
            print('Category:', out['category'])
            print('Response:', out['response'])
            if out['escalate']:
                print('(Suggested escalation to human agent)')
            print()
