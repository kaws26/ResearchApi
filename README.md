# AI Research Paper History Analysis

## 📌 Project Overview
The **AI Research Paper History Analysis** tool is a Flask-based API that retrieves research papers year-wise based on a given **category** and **topic**. It leverages **Groq's Llama-3.3-70b-versatile** model via LangChain to generate structured responses. This project was developed as part of the **ScienceHub** initiative during the **Science Day Hackathon at GGSIPU**.

## 🚀 Features
- 📚 Fetches **research papers** year-wise with researcher names.
- 🔍 Accepts **category** and **topic** as input.
- ⚡ Uses **LangChain + Groq API** for research data generation.
- 🌐 **CORS enabled** for easy frontend integration.
- 🐳 Includes a **Dockerfile** for containerization.
- 🚀 **Deployable on Render, AWS, or any cloud service**.

## 🛠️ Tech Stack
- **Backend**: Flask, LangChain, Groq API
- **Containerization**: Docker
- **Deployment**: Render (or any cloud platform)

## 📂 Project Structure
```
📁 AI-Research-History-Analysis
│── 📄 app.py              # Main Flask application
│── 📄 Dockerfile          # Docker container setup
│── 📄 .env.example        # Example environment variables file
│── 📄 requirements.txt    # Dependencies list
│── 📄 README.md           # Project documentation
```

## 🏗️ Setup & Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/kaws26/ResearchApi.git
cd AI-Research-History-Analysis
```
### 2️⃣ Install dependencies
Make sure you have **Python 3.8+** installed, then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Set up environment variables
Create a `.env` file in the project root and add:
```env
GROQ_API_KEY=your_groq_api_key
```
### 4️⃣ Run the Flask application
```bash
python app.py
```
Server will be running at: `http://0.0.0.0:5000`

## 📡 API Endpoints
### 🔹 Get Research Papers
- **Endpoint:** `/get_research`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "category": "Physics",
    "topic": "Quantum Computing"
  }
  ```
- **Response Example:**
  ```json
  {
    "research_papers": "1. 2023 - Dr. A. Smith: 'Quantum Algorithms for Optimization'\n2. 2022 - Prof. B. Kumar: 'Advancements in Quantum AI'"
  }
  ```

## 🐳 Docker Setup
### 1️⃣ Build Docker Image
```bash
docker build -t ai-research-history .
```
### 2️⃣ Run Docker Container
```bash
docker run -p 5000:5000 --env-file .env ai-research-history
```
Server will be available at `http://localhost:5000`

## 🚀 Deployment on Render
1️⃣ Create a **new Web Service** on **Render**.
2️⃣ Select your **GitHub repository**.
3️⃣ Set the **Environment Variables** (API Key).
4️⃣ Choose **Python** as runtime and deploy!

## 🛠️ Future Enhancements
- ✅ Add **caching** for better performance.
- ✅ Integrate **Google Scholar & Arxiv API** for real-time papers.
- ✅ Deploy as a **SaaS** for wider usage.

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue if you find bugs or want to request a new feature.

---

🌟 **Developed by**: Kawaljeet Singh and the ScienceHub Team 🚀

