# Simple Customer Support Chatbot

This project is a simple customer support chatbot built. It demonstrates how to classify customer questions into categories using keyword-based logic and return predefined responses. The project includes both command-line and web-based interfaces, making it easy to run locally.

---

## 📂 Project Structure

### 1. `customer_support_agent.py`

* The core chatbot logic written in Python.
* Features:

  * **Interactive CLI Mode**: Run the chatbot in the terminal and interact by typing questions.
  * **Flask API Mode**: Start a simple REST API by running `python customer_support_agent.py --api`. The API accepts POST requests with a question and returns a classified response.
* Demonstrates:

  * Keyword-based classification
  * Escalation detection for frustrated customers
  * Predefined responses for each category

### 2. `simple_chat_web.html`

* A standalone web interface for the chatbot.
* Written in **HTML, CSS, and JavaScript**.
* Features:

  * Client-side classification logic (no backend needed).
  * Simple chat-style UI to test the chatbot in the browser.

### 3. `demo_notebook.ipynb`

* A Jupyter Notebook demonstrating chatbot functionality.
* Contains sample inputs and outputs showing how the chatbot classifies questions.
* Useful for assignments, demos, or portfolio presentations.

### 4. `README.md`

* This documentation file explaining the project, its components, and usage.

### 5. `requirements.txt`

* Lists Python dependencies (`flask`) required if you want to run the chatbot as an API.

---

## 🚀 How to Run

### Option 1: Command Line Interface

```bash
python customer_support_agent.py
```

Type your question and the chatbot will respond. Type `exit` to quit.

### Option 2: Run as API

```bash
pip install -r requirements.txt
python customer_support_agent.py --api
```

The API will run at `http://127.0.0.1:5000/api/classify`.

Send a POST request with JSON:

```json
{"question": "How can I update my payment method?"}
```

### Option 3: Open in Browser

* Open `simple_chat_web.html` in any modern browser.
* Type your question and see the chatbot respond instantly.

### Option 4: Jupyter Notebook

* Open `demo_notebook.ipynb` in Jupyter.
* Run all cells to see example questions and outputs.

---

## 🧠 Chatbot Logic

* **Categories**:

  * **Billing** → e.g., payment, invoice, bill, charge
  * **Technical Support** → e.g., error, problem, not working
  * **General Inquiry** → e.g., hours, location, contact
* **Escalation Detection**:

  * If the input contains words like *angry*, *frustrated*, or *not happy*, the bot suggests escalating to a human agent.

---

## 🎯 Example Interactions

**Input**: `How can I update my payment method?`
**Output**: Billing → *For billing questions, please check your account settings or contact billing support at [billing@example.com](mailto:billing@example.com).*

**Input**: `My internet is not working.`
**Output**: Technical Support → *Please try restarting your device. If the problem persists, contact technical support at [techsupport@example.com](mailto:techsupport@example.com).*

**Input**: `I am very angry about a charge I did not make.`
**Output**: Billing + Escalation → *I understand this is frustrating. Let me connect you with a human representative. For billing questions, please check your account settings or contact billing support at [billing@example.com](mailto:billing@example.com).*

---

## 🌟 Portfolio Value

This project demonstrates:

* Python programming skills
* Use of Flask for building APIs
* Frontend development with HTML, CSS
* Notebook documentation for presentations
* Problem-solving approach in customer support automation

It can be showcased as a **portfolio project** to highlight both technical and practical application skills.

---

## 📌 Future Improvements

* Use NLP techniques (TF-IDF, ML classifiers) for more accurate classification.
* Integrate with a real database of FAQs.
* Deploy as a web app with cloud hosting.
* Add conversation history and logging.


