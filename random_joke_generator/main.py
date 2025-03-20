import streamlit as st
import requests

# Function to fetch a joke from API based on category
def get_random_joke(category="general"):
    try:
        url = (
            "https://official-joke-api.appspot.com/random_joke"
            if category == "general"
            else "https://official-joke-api.appspot.com/jokes/programming/random"
        )
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            if isinstance(joke_data, list):
                joke_data = joke_data[0]
            return f"😂 {joke_data['setup']} \n\n👉 {joke_data['punchline']}"
        else:
            return "⚠️ Failed to fetch a joke. Please try again later."
    except:
        return "💻 Why did the programmer quit his job? \nBecause he didn't get array!"

# Function to set light background with white text
def set_background(image_url):
    st.markdown(
        f"""
        <style>
            /* Background image */
            [data-testid="stAppViewContainer"] {{
                background: url({image_url}) no-repeat center center fixed;
                background-size: cover;
            }}

            /* White Text for Readability */
            * {{
                color: white !important;
            }}

            /* Joke container */
            .joke-container {{
                background: rgba(0, 0, 0, 0.7);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
                text-align: center;
                font-size: 18px;
                font-weight: bold;
            }}

            /* Centered Title */
            .title {{
                text-align: center;
                color: white;
                font-size: 36px;
                font-weight: bold;
            }}

            /* Footer Styling */
            .footer {{
                text-align: center;
                color: white;
                font-size: 14px;
                padding: 10px;
                background: rgba(0, 0, 0, 0.7);
                border-radius: 10px;
                margin-top: 20px;
            }}

            /* Black Button Text */
            div.stButton > button {{
                color: black !important;
                font-weight: bold;
                font-size: 16px;
                background-color: black !important;
                border-radius: 10px;
                padding: 10px 20px;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function
def main():
    st.set_page_config(page_title="Random Joke Generator", page_icon="😂", layout="centered")

    # Set new light background
    set_background("https://img.freepik.com/free-vector/seamless-pattern-funny-emoticons_1308-150052.jpg")

    # Title
    st.markdown("<h1 class='title'>😂 Random Joke Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Click the button below to generate a joke!</h4>", unsafe_allow_html=True)

    category = st.radio("Choose Joke Category:", ("general", "programming"), horizontal=True)

    if "joke_history" not in st.session_state:
        st.session_state.joke_history = []

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎭 Generate Joke"):
            joke = get_random_joke(category)
            st.markdown(f"<div class='joke-container'>{joke}</div>", unsafe_allow_html=True)
            st.session_state.joke_history.append(joke)

    if st.session_state.joke_history:
        st.markdown("<h3>📜 Joke History</h3>", unsafe_allow_html=True)
        with st.container():
            for idx, joke in enumerate(st.session_state.joke_history[::-1], 1):
                st.markdown(f"<div class='joke-container'>{idx}. {joke}</div>", unsafe_allow_html=True)

    st.divider()

    # Footer
    st.markdown(
        """
        <div class="footer">
            <p>Jokes from <a href='https://official-joke-api.appspot.com/' target='_blank' style='color: yellow;'>Official Joke API</a></p>
            <p>Built with ❤️ by <strong>Saba Muhammad Riaz</strong> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()







