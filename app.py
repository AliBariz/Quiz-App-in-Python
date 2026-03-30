import streamlit as st
import random
import time
from datetime import datetime, timedelta

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'questions_shuffled' not in st.session_state:
    st.session_state.questions_shuffled = False

# Sample questions data
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Oganesson"],
        "correct_answer": "Oxygen"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
        "correct_answer": "Vatican City"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Tomato", "Avocado", "Onion", "Chili"],
        "correct_answer": "Avocado"
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "correct_answer": "JavaScript"
    },
    {
        "question": "How many bones are there in the human body?",
        "options": ["206", "208", "210", "212"],
        "correct_answer": "206"
    }
]

def shuffle_questions():
    """Shuffle the questions randomly"""
    shuffled = QUESTIONS.copy()
    random.shuffle(shuffled)
    return shuffled

def calculate_score(questions, user_answers):
    """Calculate the final score"""
    correct = 0
    for i, q in enumerate(questions):
        if user_answers.get(i) == q['correct_answer']:
            correct += 1
    return correct

def restart_quiz():
    """Reset all quiz state"""
    st.session_state.current_question = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.start_time = datetime.now()
    st.session_state.questions_shuffled = True

def next_question():
    """Move to next question"""
    if st.session_state.current_question < len(st.session_state.questions) - 1:
        st.session_state.current_question += 1

def prev_question():
    """Move to previous question"""
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

def submit_quiz():
    """Submit the quiz"""
    st.session_state.quiz_submitted = True

# Main app
def main():
    st.set_page_config(
        page_title="Quiz Application",
        page_icon="❓",
        layout="centered"
    )

    # Custom CSS styling
    st.markdown("""
<style>
    /* Main container */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0px;
    }

    /* Question card styling */
    .question-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }


    /* Button styling */
    .stButton>button {
        border-radius: 25px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    /* Radio button styling */
    .stRadio > div {
        gap: 10px;
    }

    .stRadio > div > label {
        border-radius: 10px;
        padding: 12px 15px;
        margin: 5px 0;
        border: 2px solid #e0e0e0;
        transition: all 0.2s ease;
    }

    .stRadio > div > label:hover {
        border-color: #4F8BF9;
        background-color: #0000;
    }

    /* Correct/incorrect answer styling */
    .correct-answer {
        background-color: #d4edda !important;
        border-color: #28a745 !important;
        color: #155724 !important;
    }

    .incorrect-answer {
        background-color: #f8d7da !important;
        border-color: #dc3545 !important;
        color: #721c24 !important;
    }

    /* Score display */
    .score-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 30px;
        color: white;
        text-align: center;
        margin: 20px 0;
    }

    .score-number {
        font-size: 3em;
        font-weight: bold;
        margin: 10px 0;
    }

    /* Timer styling */
    .timer-display {
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
        color: #495057;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

    # Header
    st.title("❓ Interactive Quiz Application")
    st.markdown("---")

    # Initialize questions if not already shuffled
    if not st.session_state.questions_shuffled:
        st.session_state.questions = shuffle_questions()
        st.session_state.questions_shuffled = True
        st.session_state.start_time = datetime.now()

    questions = st.session_state.questions

    # Timer display
    if st.session_state.start_time:
        elapsed = datetime.now() - st.session_state.start_time
        minutes, seconds = divmod(int(elapsed.total_seconds()), 60)
        st.markdown(f"<div class='timer-display'>⏱️ Time Elapsed: {minutes:02d}:{seconds:02d}</div>", unsafe_allow_html=True)

    # Progress bar
    progress = (st.session_state.current_question + 1) / len(questions)
    st.progress(progress)
    st.caption(f"Question {st.session_state.current_question + 1} of {len(questions)}")

    if not st.session_state.quiz_submitted:
        # Display current question
        current_q = questions[st.session_state.current_question]

        st.markdown("<div class='question-card'>", unsafe_allow_html=True)
        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(current_q["question"])

        # Radio buttons for options
        selected_option = st.radio(
            "Choose your answer:",
            current_q["options"],
            key=f"q_{st.session_state.current_question}",
            index=[i for i, opt in enumerate(current_q["options"])
                  if opt == st.session_state.user_answers.get(st.session_state.current_question, "")][0]
                 if st.session_state.user_answers.get(st.session_state.current_question, "") in current_q["options"] else None
        )

        # Store user answer
        if selected_option:
            st.session_state.user_answers[st.session_state.current_question] = selected_option

        st.markdown("</div>", unsafe_allow_html=True)

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.button("← Previous", on_click=prev_question,
                     disabled=st.session_state.current_question == 0)

        with col2:
            if st.session_state.current_question == len(questions) - 1:
                st.button("Submit Quiz 📝", on_click=submit_quiz)

        with col3:
            st.button("Next →", on_click=next_question,
                     disabled=st.session_state.current_question == len(questions) - 1)

    else:
        # Quiz submitted - show results
        st.markdown("<div class='question-card'>", unsafe_allow_html=True)
        st.subheader("🎉 Quiz Completed!")

        # Calculate scores
        total_questions = len(questions)
        correct_answers = calculate_score(questions, st.session_state.user_answers)
        wrong_answers = total_questions - correct_answers

        # Display summary
        st.markdown(f"""
        <div class='score-container'>
            <h2>Your Score</h2>
            <div class='score-number'>{correct_answers}/{total_questions}</div>
            <p><strong>{round((correct_answers/total_questions)*100, 1)}%</strong></p>
        </div>
        """, unsafe_allow_html=True)

        st.write(f"**Total Questions:** {total_questions}")
        st.write(f"**Correct Answers:** {correct_answers}")
        st.write(f"**Wrong Answers:** {wrong_answers}")

        st.markdown("</div>", unsafe_allow_html=True)

        # Show detailed results
        st.subheader("Detailed Results:")

        for i, q in enumerate(questions):
            user_answer = st.session_state.user_answers.get(i, "Not answered")
            is_correct = user_answer == q['correct_answer']

            # Determine styling classes
            if is_correct:
                bg_class = "correct-answer"
                icon = "✅"
                status = "Correct"
            else:
                bg_class = "incorrect-answer"
                icon = "❌"
                status = "Incorrect"

            st.markdown(f"""
            <div class='question-card {bg_class}'>
                <strong>Question {i+1}: {q['question']}</strong><br><br>
                <strong>Your Answer:</strong> {user_answer} {icon}<br>
                <strong>Status:</strong> {status}
                """, unsafe_allow_html=True)

            if not is_correct:
                st.markdown(f"<strong>Correct Answer:</strong> {q['correct_answer']}", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.button("Restart Quiz 🔄", on_click=restart_quiz)

    # Closing main container div
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()