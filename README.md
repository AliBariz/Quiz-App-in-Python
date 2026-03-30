# 🧠 Streamlit Quiz App

An interactive and user-friendly **Quiz Application** built using **Python** and **Streamlit**. This app presents multiple-choice questions with a clean UI, tracks progress, and displays results instantly.

---

## 🚀 Features

* ✅ Multiple-choice quiz (MCQs)
* 🎯 One question at a time
* ⏭️ Next / Previous navigation
* 📊 Progress bar indicator
* 🧮 Real-time score calculation
* 🎉 Final results summary
* 🔄 Restart quiz option
* 🎨 Clean and modern UI with custom styling
* 🔀 Questions shuffled on each run

---

## 🖼️ UI Highlights

* Responsive layout using Streamlit components
* Card-style question display
* Colored feedback:

  * 🟢 Correct answers
  * 🔴 Incorrect answers
* Smooth user experience with session state handling

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**

---

## 📦 Installation

1. Clone the repository:

   ```bash
   https://github.com/AliBariz/Quiz-App-in-Python.git
   cd quiz-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install streamlit
   ```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
quiz-app/
│── app.py          # Main Streamlit app
│── README.md       # Project documentation
```

---

## 🧪 Example Questions

* General Knowledge
* Science
* Technology
* Customizable question sets

---

## 🔧 Customization

You can easily modify the quiz by editing the question list inside `app.py`:

```python
questions = [
    {
        "question": "Your question here?",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
    }
]
```

---

## 💡 Future Improvements

* ⏱️ Timer per question
* 🌐 Database integration
* 📈 Performance analytics
* 👤 User authentication

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
