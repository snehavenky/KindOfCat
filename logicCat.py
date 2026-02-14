import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="What Cat Are You?", page_icon="🐾")

st.title("🐾 Which Cat Breed Are You?")
st.subheader("Answer 5 questions to find your feline alter-ego!")

# --- UI: DROP DOWN QUESTIONS ---
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

# --- SCORING LOGIC ---
# We map each answer to specific cat "points"
cat_data = {
    "Maine Coon": {"desc": "A gentle giant! You are social, kind, and surprisingly mellow despite your big presence.", "points": 0},
    "Siamese": {"desc": "The chatterbox! You are vocal, opinionated, and love being the center of attention.", "points": 0},
    "Persian": {"desc": "Royal & Elegant. You prefer the finer things in life and a quiet, luxurious nap over chaos.", "points": 0},
    "Bengal": {"desc": "The wild child! You are high-energy, adventurous, and probably a bit athletic.", "points": 0},
    "Sphynx": {"desc": "Unique and clingy! You march to the beat of your own drum and crave constant warmth and love.", "points": 0},
    "Ragdoll": {"desc": "Ultimate chill. You are laid-back, affectionate, and handle stress by just going limp.", "points": 0},
    "Scottish Fold": {"desc": "Sweet and curious. You are an observer who loves cozy spots and gentle play.", "points": 0},
    "Russian Blue": {"desc": "The quiet intellectual. You are a bit shy with strangers but fiercely loyal to your inner circle.", "points": 0},
    "Abyssinian": {"desc": "The busy bee! You are always on the move, exploring every nook and cranny of your world.", "points": 0},
    "British Shorthair": {"desc": "Dignified and calm. You have a dry sense of humor and value your independence.", "points": 0}
}

if st.button("Reveal My Inner Cat"):
    if "Select an option" in [color, angry, sad, happy, excited]:
        st.warning("Please answer all the questions first!")
    else:
        # Simple Logic Mapping
        if color == "Orange": cat_data["Maine Coon"]["points"] += 1
        if angry == "Knock things over": cat_data["Bengal"]["points"] += 2
        if happy == "Relax in the sun": cat_data["Persian"]["points"] += 2
        if sad == "Seek cuddles": cat_data["Ragdoll"]["points"] += 2
        if excited == "Chirp/Talk a lot": cat_data["Siamese"]["points"] += 2
        if excited == "Get chaotic": cat_data["Bengal"]["points"] += 1
        if excited == "Jump for joy": cat_data["Abyssinian"]["points"] += 1
        if angry == "Silent treatment": cat_data["British Shorthair"]["points"] += 2
        if sad == "Sleep all day": cat_data["Russian Blue"]["points"] += 1
        
        # Tie-breaker logic: select the cat with the most points
        # If all 0, it defaults to a fun random choice
        winner = max(cat_data, key=lambda x: cat_data[x]["points"])
        
        st.divider()
        st.balloons()
        st.header(f"You are a {winner}!")
        st.write(cat_data[winner]["desc"])

st.divider()
st.caption("No API calls used - 100% locally calculated!")
