
# Simple Customer Support Chatbot
Files included:
- customer_support_agent.py : Python CLI + optional Flask API (run with `python customer_support_agent.py --api`)
- simple_chat_web.html : Standalone client-side webpage (open in browser)
- demo_notebook.ipynb : Jupyter notebook demonstrating sample inputs/outputs
- requirements.txt : Python dependencies for the API (Flask)

Usage:
1. CLI: `python customer_support_agent.py` and type questions interactively.
2. API: `pip install -r requirements.txt` then `python customer_support_agent.py --api` to run a local server.
   POST JSON to /api/classify with {"question": "your question"}.
3. Webpage: open `simple_chat_web.html` in a browser (client-side only).
