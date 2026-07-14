# 🏗️ Raajakalpa Financial Intelligence

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

> **An enterprise-grade, interactive financial dashboard for tracking, auditing, and analyzing residential construction expenditures.**

The application bridges the gap between structured tabular data analytics and unstructured data querying by integrating a LangChain-powered **Retrieval-Augmented Generation (RAG)** pipeline, allowing project managers to natively chat with their underlying financial ledgers.

---

## ✨ Core Features

* **🖥️ Enterprise User Interface:** Clean, minimalist styling utilizing custom CSS and a tabbed navigation system to logically separate executive KPI overviews, deep-dive tabular data, and AI interactions.
* **📊 Interactive Visual Analytics:** Dynamic Plotly-driven visualizations, including an expenditure hierarchy Treemap and a modular Donut chart, for instant financial distribution insights.
* **📥 Dynamic Data Export:** Real-time Pandas dataframe filtering with secure, on-the-fly CSV generation for exporting audited line items.
* **🤖 RAG-Powered AI Consultant:** A fully integrated chat interface backed by Google's Gemini models, enabling users to ask highly specific questions about materials, contractors, or ledger calculations directly against the raw text logs.

---

## 🧠 Architecture: How the RAG Pipeline Works

The integrated AI assistant relies on a Retrieval-Augmented Generation (RAG) architecture to provide accurate, fact-grounded answers based strictly on the project's private ledger data. 

Here is the step-by-step technical execution within the application:

1. **Document Ingestion (`TextLoader`):** The raw, unstructured financial logs (`raajakalpa_budget.txt`) are ingested into the LangChain ecosystem. This file serves as the definitive ground-truth context for the AI.
2. **Semantic Vectorization (`GoogleGenerativeAIEmbeddings`):** The loaded text is processed by Google's embedding model. This converts the textual ledger data into high-dimensional numerical vectors, capturing the semantic meaning and contextual relationships of the financial entries.
3. **Vector Indexing (`VectorstoreIndexCreator`):** The generated embeddings are compiled into a searchable, in-memory vector database. When a user asks a question, this index performs a similarity search to retrieve only the specific text chunks most relevant to the user's query, ensuring efficiency and accuracy.
4. **Generative Synthesis (`ChatGoogleGenerativeAI`):** The retrieved context chunks are combined with the user's original query and passed to the Gemini Large Language Model. The LLM processes this isolated context to generate a highly precise, human-readable response without hallucinating outside information.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend UI & Routing** | Streamlit |
| **Data Manipulation** | Pandas |
| **Interactive Visualization** | Plotly Express |
| **AI Orchestration** | LangChain (`langchain-community`, `langchain-classic`) |
| **LLM & Embeddings** | Google GenAI API (`langchain-google-genai`) |
| **Environment Management** | Python-dotenv |

---

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/shashank-333/raajakalpa-analytics.git](https://github.com/shashank-333/raajakalpa-analytics.git)
cd raajakalpa-analytics
