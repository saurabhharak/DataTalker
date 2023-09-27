# DataTalker

## Introduction

DataTalker is a Streamlit web application that allows users to have a conversation with their dataset. It leverages the LangChain library to facilitate natural language interactions with the data.

## Features

- Upload CSV or Excel datasets.
- Chat with your dataset using natural language queries.
- Retrieve responses based on your questions.

## Requirements

To run DataTalker, you'll need:

- Python 3.6 or higher.
- The following Python packages:
  - streamlit
  - pandas
  - langchain

## Installation

You can install the required packages using `pip`:

```bash
pip install streamlit pandas langchain
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/saurabhharak/DataTalker.git
cd DataTalker
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open your web browser and navigate to `http://localhost:8501`.

## Instructions

1. Upon launching the app, you'll be greeted with a welcome message.

2. On the sidebar, use the "Upload Dataset" section to upload your dataset in either CSV or Excel format.

3. In the "Instructions" section, you'll find details on how to obtain a free API key from OpenAI.

4. Enter your OpenAI API key in the text input provided.

5. You can now start conversing with your dataset! Type a question in the chat input box and press Enter to send it.

6. The assistant will respond based on the message you provide.

## Example Conversation

User: "What is the average age of the employees?"

Assistant: "The average age of the employees is 35 years."

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [LangChain](https://github.com/langchain/langchain)

## Contact

For questions or support, please contact [jobsforsaurabhharak@gmail.com](mailto:jobsforsaurabhharak@gmail.com).

---
