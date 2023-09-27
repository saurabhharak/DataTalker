import streamlit as st
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
# Function to get dataset from user
def get_user_dataset():
    st.sidebar.header("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            return df
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
    return None

# Function to initialize or retrieve agent
def get_agent(df, openai_api_key):
    if "agent" not in st.session_state:
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0, openai_api_key=openai_api_key), df, verbose=True)
        st.session_state.agent = agent
    return st.session_state.agent

# Main Streamlit app
def main():
    st.set_page_config(
        page_title="DataTalker: Have a Conversation with Your Dataset",
        page_icon=":speech_balloon:",
    )
    st.title("Welcome to DataTalker")
    # Provide user instructions
    st.sidebar.header("Instructions")
    #st.sidebar.markdown(
        #"1. Use the sidebar to upload a CSV or Excel file containing your dataset.\n"
        #"2. Once the dataset is uploaded, you can start chatting with it!\n"
        #"3. Type your message in the chat input box and press Enter to send it.\n"
        #"4. The assistant will respond based on the message you provide.\n"
    #S)
    st.sidebar.write("\n\n")
    st.sidebar.markdown("**Get a free API key from OpenAI:**")
    st.sidebar.markdown("* Create a [free account](https://platform.openai.com/signup?launch) or [login](https://platform.openai.com/login)")
    st.sidebar.markdown("* Go to **Personal** and then **API keys**")
    st.sidebar.markdown("* Create a new API")
    st.sidebar.markdown("* Paste your API key in the text box")
    st.sidebar.divider()
    # Get OpenAI API Key from user
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key")

    # Get or upload dataset
    df = get_user_dataset()
    if df is None:
        return

    # Initialize or retrieve agent
    agent = get_agent(df, openai_api_key)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask a question about your dataset"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = agent.run(prompt)
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split('n/'):
                full_response += chunk + " "
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
