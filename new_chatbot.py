import nltk
import streamlit as st
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs =[
    [
        r"(hi|hello|hey|good morning|good afternoon|good evening)",
        ["Hello! This is the Anime Guide for beginners. How can I assist you today?", "Hi there! How can I help you broaden your knowledge on anime?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm here to assist you with any anime inquiries!", "I'm doing great! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I am your virtual anime guide.", "You can call me AnimeBot, your personal anime guide!"]
    ],
    [
        r"(what is anime|anime\??)",
        ["Anime is a style of animation that originated in Japan. Unlike Western cartoons, anime often includes complex characters, mature themes, and visually rich storytelling. Anime spans many genres and targets various age groups—from children to adults. Some anime are adapted from manga (Japanese comics), light novels, or video games."]
    ],
    [
        r"(what are good anime recommendations\??|recommendation)",
        ["Here are some great starter anime based on genres:\n\n" +
         "**Action/Adventure:** Naruto, My Hero Academia, Attack on Titan, Fullmetal Alchemist: Brotherhood\n" 
         "\n**Slice of Life/Comedy:** Spy x Family, K-On!, Nichijou, Barakamon\n" 
         "\n**Romance/Drama:** Your Lie in April, Toradora!, Clannad, Horimiya\n" 
         "\n**Fantasy/Isekai:** That Time I Got Reincarnated as a Slime, Re:Zero, Sword Art Online\n" 
         "\n**Mystery/Psychological:** Death Note, Steins;Gate, Erased\n" 
         "\n**Light-Hearted:** My Neighbour Totoro, Fruits Basket, The Disastrous Life of Saiki K."]
    ],
    [
        r"(i want action genre\??|action)",
        ["Sure! Here are some great action anime for beginners:\n- Naruto\n- My Hero Academia\n- Attack on Titan\n- Fullmetal Alchemist: Brotherhood"]
    ],
    [
        r"(i want slice of life / comedy\??|slice of life|comedy)",
        ["Here are some relaxing and fun slice of life/comedy anime:\n- Spy x Family\n- K-On!\n- Nichijou (My Ordinary Life)\n- Barakamon"]
    ],
    [
        r"(romance|romance anime|drama)",
        ["If you're into romance or drama, try these:\n- Your Lie in April\n- Toradora!\n- Clannad\n- Horimiya"]
    ],
    [
        r"(fantasy|isekai|other worlds)",
        ["Fantasy/isekai anime recommendations:\n- That Time I Got Reincarnated as a Slime\n- Re:Zero\n- Sword Art Online\n- No Game No Life"]
    ],
    [
        r"(mystery|psychological)",
        ["For mystery or psychological anime, check out:\n- Death Note\n- Steins;Gate\n- Erased\n- Paranoia Agent"]
    ],
    [
        r"(anime for kids|younger viewers)",
        ["Great anime for younger viewers:\n- Pokémon\n- Digimon\n- Doraemon\n- Beyblade"]
    ],
    [
        r"(feel good|light hearted)",
        ["Feel-good anime recommendations:\n- My Neighbour Totoro\n- Fruits Basket\n- Natsume’s Book of Friends\n- The Disastrous Life of Saiki K."]
    ],
    [
        r"(genres|anime genres)",
        ["Common anime genres explained:\n\n" +
         "- **Shounen:** Action, friendship, growth (e.g., Naruto)\n" +
         "- **Shoujo:** Romance, emotional development (e.g., Sailor Moon)\n" +
         "- **Seinen:** Mature themes for adult men (e.g., Berserk)\n" +
         "- **Josei:** Realistic romance for adult women (e.g., Nana)\n" +
         "- **Isekai:** Transported to another world (e.g., Re:Zero)\n" +
         "- **Mecha:** Robots and machines (e.g., Gundam)\n" +
         "- **Slice of Life:** Everyday life stories (e.g., March Comes in Like a Lion)\n" +
         "- **Sports:** Competitive sports (e.g., Haikyuu!!)"]
    ],
    [
        r"(where to watch|streaming|legal sites)",
        ["Legal anime streaming platforms:\n" +
         "- **Crunchyroll:** Large library, free with ads or premium\n" +
         "- **Funimation:** Dubbed and subbed anime\n" +
         "- **Netflix:** Mix of original and licensed anime\n" +
         "- **HiDive:** Niche and older titles\n" +
         "- **Amazon Prime Video:** Exclusives like Vinland Saga\n" +
         "- **YouTube:** Some official channels stream episodes"]
    ],
    [
        r"(subbed or dubbed|watch in japanese)",
        ["You can choose either! Subbed means Japanese with English subtitles, while dubbed has English voiceovers. It's all about personal preference."]
    ],
    [
        r"(how long is anime|episodes)",
        ["Most anime have 12 or 24 episodes per season. Some long-running shows (like One Piece) have hundreds of episodes."]
    ],
    [
        r"(anime for kids only|is anime for kids)",
        ["Not at all! Anime covers all age ranges and themes—from fun and silly to dark and serious."]
    ],
    [
        r"(manga|read manga first)",
        ["You can start with anime without reading manga. Anime stands on its own, though manga sometimes offers more detail."]
    ],
    [
        r"(what('s| is) the difference (between|of) (anime|japanese animation) (and|&|vs) (cartoons|cartoon|western animation)|(anime vs cartoon))",
        ["While both are animated, anime tends to focus more on deep plots, emotions, and character development. It's also culturally tied to Japan."]
    ],
    [
        r"(thank you|thanks)",
        ["You're welcome! Enjoy your anime journey!", "Happy to help! Let me know if you need more recommendations."]
    ],
    [
        r"(quit|exit|bye)",
        ["Thanks for chatting! Hope you find an anime you love!", "Goodbye! Come back anytime for more anime tips."]
    ],
    [
        r".*",
        ["I'm not sure I understand. Could you ask about anime genres, recommendations, or where to watch?", "I specialize in anime! Try asking for recommendations or anime basics."]
    ]
]


# Create a Chat object
chatbot = Chat(pairs, reflections)

# Streamlit app
def main():
    st.title("Anime Chatbot")
    st.write("Welcome to the chatbot. What do you want to know about anime ")

    # Initialize session state to store chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input from user
    user_input = st.text_input("You: ")

    if user_input:
        # Get chatbot response
        response = chatbot.respond(user_input)
        st.session_state.history.append(f"You: {user_input}")
        st.session_state.history.append(f"ChatBot: {response}")

    # Display chat history
    for message in st.session_state.history:
        st.write(message)

if __name__ == "__main__":
    main()