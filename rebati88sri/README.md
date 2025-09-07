# 🌐 WORLD ATM SIMULATOR (Advanced Version)

### 🎥 Demo Video
[Watch Demo on YouTube](https://youtu.be/MRe4Wz6jZA8)

---

## 📌 Description
**World ATM Simulator** is a Python-based CLI application that simulates the behavior of an ATM. With enhanced features like admin control, real user data persistence, and multi-functionality, it's a comprehensive final project submission for CS50P.

---

## 💡 Features

- 🔐 PIN verification (with lockout after 3 failed attempts)
- 👥 Multiple user support with persistent storage (`users.json`)
- 💰 Deposit & Withdraw (with ₹100 multiples and min balance rule)
- 📜 Transaction History with timestamps
- 🎨 Color-coded interface using `colorama`
- 🔄 Currency converter (INR to USD)
- 🧑‍💼 Admin Mode to add/view users
- 🧪 Pytest-based unit tests

---

## 📁 File Overview

| Filename              | Purpose                                  |
|----------------------|-------------------------------------------|
| `atm_simulator.py`   | Main application logic                   |
| `test_atm_simulator.py` | Unit tests for functions                 |
| `users.json`         | Persistent storage of users              |
| `requirements.txt`   | Python dependencies                      |
| `README.md`          | Project documentation                    |

---

## 🛠️ Setup Instructions

```bash
# Clone or download the repository
pip install -r requirements.txt
python atm_simulator.py
```

---

## 🧪 Run Tests

```bash
pytest test_atm_simulator.py
```

---

## 📌 Sample Admin Login

Username: `admin`
(You will be prompted for options to view or add users)

---

## 📸 Screenshots

> Add screenshots or a GIF showing terminal interaction

---

## 📈 Future Improvements
- OTP/2FA
- SQLite database
- GUI version with Tkinter

---

## 🏅 CS50P Final Project Submission Checklist
- [x] Problem inspired by real-world scenario
- [x] Modularized code with defined functions
- [x] Contains input validation
- [x] Uses external libraries (e.g., `colorama`)
- [x] Includes test cases
- [x] Has clear README and video

✅ You're ready to resubmit!
