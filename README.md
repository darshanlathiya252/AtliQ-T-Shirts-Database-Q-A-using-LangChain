# AtliQ-T-Shirts-Database-Q-A-using-LangChain
👕 AtliQ T-Shirts: Database Q&A using LangChain

An AI-powered Question Answering system that allows users to ask natural language questions about a MySQL database containing T-shirt inventory data.
The system automatically converts user questions into SQL queries, executes them, and returns clear, human-readable answers.

Built using LangChain, OpenRouter (GPT-3.5), Few-Shot Prompting, Vector Similarity (Chroma), and Streamlit.

🚀 Features

🔍 Ask questions in plain English

🧠 Automatic SQL query generation using LLMs

📊 Real-time MySQL database querying

🧩 Few-shot prompting with semantic similarity

📚 Vector database (Chroma) for example selection

🌐 Interactive web UI using Streamlit

🔐 Secure API key management using .env

🏗️ Tech Stack
Layer	Technology
LLM	OpenAI GPT-3.5 (via OpenRouter)
Framework	LangChain
Database	MySQL
ORM	SQLAlchemy
Vector Store	Chroma
Embeddings	Sentence Transformers
Frontend	Streamlit
Language	Python
📁 Project Structure
<img width="394" height="205" alt="image" src="https://github.com/user-attachments/assets/2e076c23-c45e-45e4-be7b-ed89bdfb7d7e" />

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/atliq-tshirts-qa.git
cd atliq-tshirts-qa

2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file in the project root:

api_key=sk-or-xxxxxxxxxxxxxxxxxxxx


⚠️ Do not share or commit this file.

5️⃣ Configure MySQL Database

Update database credentials inside langchain_helper.py:

db_user = "root"
db_password = "root"
db_host = "127.0.0.1"
db_name = "atliq_tshirts"


Make sure the database and tables exist before running the app.

6️⃣ Run the Streamlit App
python -m streamlit run main.py


The app will open at:

http://localhost:8501

🧪 Example Questions

How many total T-shirts are left in stock?

How many Nike T-shirts are available in white color?

What is the total stock for size XS?

How many Levi T-shirts do we have?

🧠 How It Works

User enters a natural language question

Relevant few-shot examples are selected using vector similarity

LangChain generates a syntactically correct SQL query

Query is executed on the MySQL database

The result is converted into a user-friendly answer

🔒 Security Notes

API keys are stored securely using environment variables

.env is excluded from version control

Only read-only SQL queries are generated

📌 Future Improvements

🔐 Role-based database access

💬 Chat-style interface

📈 Query performance caching

🐳 Docker deployment

☁️ Cloud database integration

🤝 Contributing

Contributions, suggestions, and improvements are welcome.
Feel free to open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License.

⭐ Acknowledgements

LangChain

OpenAI / OpenRouter

Streamlit

Sentence Transformers
