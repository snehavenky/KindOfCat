import streamlit as st
import google.generativeai as genai

# --- APP CONFIGURATION ---
st.set_page_config(page_title="What Cat Are You?", page_icon="🐾")

# Sidebar for API Key
with st.sidebar:
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Get an API key at [Google AI Studio](https://aistudio.google.com/)")

# --- UI DESIGN ---
st.title("🐾 Which Cat Breed Are You?")
st.subheader("Answer 5 questions to find your feline alter-ego!")

# Questions & Dropdown Options
color = st.selectbox("1. What is your favorite color?", 
                    ["Select an option", "Orange", "Midnight Black", "Pure White", "Silver Grey", "Golden Brown", "Multi-colored"])

angry = st.selectbox("2. What do you do when you are angry?", 
                    ["Select an option", "Hiss/Yell", "Hide in a corner", "Silent treatment", "Knock things over", "Nap it off"])

sad = st.selectbox("3. What do you do when you are sad?", 
                  ["Select an option", "Seek cuddles", "Eat snacks", "Stare out the window", "Sleep all day", "Cry loudly"])

happy = st.selectbox("4. What do you do when you are happy?", 
                    ["Select an option", "Run around (Zoomies)", "Purr/Hum", "Share gifts", "Show off", "Relax in the sun"])

excited = st.selectbox("5. What do you do when you are excited?", 
                      ["Select an option", "Jump for joy", "Chirp/Talk a lot", "Tail twitching", "Invite others to play", "Get chaotic"])

# The 10 Possible Cats
cat_options = [
    "Maine Coon", "Siamese", "Persian", "Bengal", "Sphynx", 
    "Ragdoll", "Scottish Fold", "Russian Blue", "Abyssinian", "British Shorthair"
]

# --- LOGIC ---
if st.button("Reveal My Inner Cat"):
    if not api_key:
        st.error("Please provide an API key in the sidebar!")
    elif "Select an option" in [color, angry, sad, happy, excited]:
        st.warning("Please answer all the questions first!")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Create the Prompt
            prompt = f"""
            Based on these personality traits:
            - Favorite Color: {color}
            - Reaction to Anger: {angry}
            - Reaction to Sadness: {sad}
            - Reaction to Happiness: {happy}
            - Reaction to Excitement: {excited}

            Pick exactly ONE cat breed from this list that best matches this person: {', '.join(cat_options)}.
            
            Provide the output in this format:
            ## You are a [Breed Name]!
            **Why?** [A short, 2-sentence witty explanation of why they match this cat.]
            """

            with st.spinner("Consulting the Cat Council..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- FOOTER ---
st.divider()
st.caption("Powered by Gemini 1.5 Flash")
