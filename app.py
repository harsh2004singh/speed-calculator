import streamlit as st
import random
import time

# ---------- Functions ----------
def mistake(paragraphtest, usertest):
    error = 0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_calculator(time_start, time_end, userinput):
    time_delay = time_end - time_start
    speed = len(userinput) / time_delay
    return round(speed, 2)

# ---------- Word List ----------
test_strings = [("I met a traveller from an antique land, Who said, 'Two vast and trunkless legs of stone Stand in the desert. Near /n"
        " them, on the sand,Half sunk, a shattered visage lies, whose frown,And wrinkled lip, and sneer of cold command, /n"
         "Tell that its sculptor well those passions read Which yet survive, stamped on these lifeless things,The hand that /n"
         " mocked them, and the heart that fed; And on the pedestal these words appear: 'My name is Ozymandias, king of kings:  /n"
         "Look on my works, ye Mighty, and despair!' Nothing beside remains. Round the decay Of that Colossal Wreck, boundless and /n"
         "bare,The lone and level sands stretch far away."),
        ("The mountains tell me, hold your head high Whatever be the problem, look it in the eye. The rivers tell me, don't look /n"
         "behind. March on ahead, till your goal you find. The sea tells me, have depth of character.The waves call out, don't forget /n"
         " your laughter! The trees tell me, do good to one and all. Let go of the past, like I let my leaves fall.The sun tells me, you /n "
         "must go on shining. In every dark cloud, be the silver lining. Have a look at nature, and you will see,There's so much to learn, just like me!"),
        ("Do not stand By my grave, and weep. I am not there, I do not sleep- I am the thousand winds that blow I am the diamond glints in snow /n"
         "I am the sunlight on ripened grain, I am the gentle, autumn rain. As you awake with morning’s hush, I am the swift up-flinging rush Of quiet /n "
         "birds in circled flight, I am the day transcending soft night. Do not stand  By my grave, and cry-I am not there.I did not die."),
        ("Never shall I forget that night, the first night in camp, that turned my life into one long night seven times sealed. Never shall I forget that/n"
         " smoke. Never shall I forget the small faces of the children whose bodies I saw transformed into smoke under a silent sky. Never shall I forget /n"
         " those flames that consumed my faith for ever. Never shall I forget the nocturnal silence that deprived me for all eternity of the desire to live. /n"
         "Never shall I forget those moments that murdered my God and my soul and turned my dreams to ashes. Never shall I forget those things, even were I/n"
         " condemned to live as long as God Himself. Never."),
        ("How do I love thee? Let me count the ways. I love thee to the depth and breadth and height My soul can reach, when feeling out of sight For the /n"
         "ends of being and ideal grace. I love thee to the level of every day's Most quiet need, by sun and candlelight.I love thee freely, as men strive for right; /n"
         "I love thee purely, as they turn from Praise. I love with a passion put to use In my old griefs, and with my childhood's faith. I love thee with a love I /n"
         "seemed to lose With my lost saints, I love thee with the breath, Smiles, tears, of all my life! and, if God choose, I shall but love thee better after death.")]

# ---------- Session State Safe Init ----------
if 'random_string' not in st.session_state:
    st.session_state['random_string'] = random.choice(test_strings)

if 'start_time' not in st.session_state:
    st.session_state['start_time'] = 0

# ---------- UI ----------
st.title("⌨️ Typing Speed Calculator")

st.subheader("Type this word 👇")
st.text_area(
    "Type this paragraph 👇",
    st.session_state['random_string'],
    height=200,
    disabled=True
)

user_input = st.text_area("Start typing here:", height=200)


# Start timer when user starts typing
if user_input != "" and st.session_state['start_time'] == 0:
    st.session_state['start_time'] = time.time()

# Submit Button
if st.button("Submit"):
    if st.session_state['start_time'] != 0:

        end_time = time.time()
        speed = speed_calculator(
            st.session_state['start_time'], end_time, user_input
        )
        errors = mistake(st.session_state['random_string'], user_input)

        st.success(f"Speed: {speed} characters/sec")
        st.error(f"Errors: {errors}")

        # reset for next round
        st.session_state['random_string'] = random.choice(test_strings)
        st.session_state['start_time'] = 0
