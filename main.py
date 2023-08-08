import streamlit as st
import openai

# API key
api_key = "API_KEY"  # Hide API key because of privacy reasons replace it with your own api
openai.api_key = api_key


# Function to interact with api and get a response
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            stop=None,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"


# Streamlit app
def main():
    st.title("PyBot.Ai")
    st.write("Ask me anything!:")

    user_input = st.text_area("You:", value="", height=100)

    if st.button("Send"):
        if user_input.strip() != "":
            bot_response = get_gpt_response(user_input)
            st.text_area("Bot:", value=bot_response, height=200)


if __name__ == "__main__":
    main()
