# GitHub Repository Setup Guide 🚀

This guide will help you clone, set up, and manage the QuiverAgent project from the GitHub repository.

---

## 📋 Prerequisites

- **Git** installed on your system.  
- **Python 3.8+** installed.  
- A **GitHub account** with access to the repository.

---

## 🚀 Cloning the Repository

1️⃣ Open your terminal and run:

```bash
git clone https://github.com/your-username/QuiverAgent.git
cd QuiverAgent
```

2️⃣ Check the Git status:

```bash
git status
```

This will show you the current branch and any modified files.

---

## ⚙️ Setting Up the Project

### 🔹 Virtual Environment (venv) Setup

1️⃣ **Create a Virtual Environment:**

```bash
python -m venv venv
```

2️⃣ **Activate the Virtual Environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

3️⃣ **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4️⃣ **When to Include/Exclude `venv/`:**  
- ✅ **Include `venv/`** if sharing with non-technical users or replicating an exact environment.  
- 🚫 **Exclude `venv/`** (recommended) for standard sharing. Use `requirements.txt` for dependency installation.

---

## 🔄 Managing Git Changes

### 🔹 Handling `.git/` Directory

- The `.git/` directory is essential for tracking changes and syncing with GitHub.  
- **Important:** Your `.git` directory will **expire in 6 days** (as per the current configuration). Ensure all changes are pushed before then.

### 🔹 Basic Git Commands

1️⃣ **Check for Changes:**

```bash
git status
```

2️⃣ **Add and Commit Changes:**

```bash
git add .
git commit -m "Your commit message"
```

3️⃣ **Push Changes to GitHub:**

```bash
git push origin main
```

4️⃣ **Pull Latest Changes:**

```bash
git pull origin main
```

---

## 💾 Working with the Database

1️⃣ **Initialize the Database:**

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

2️⃣ **Run the App:**

```bash
flask run
```

Access the app at `http://127.0.0.1:5000`.

---

## ⚡ Notes

- Run `pip install --upgrade pip` if you encounter issues with dependencies.  
- Keep `.git` and `venv` in your local environment but avoid including them when sharing the project publicly.

Happy Coding! 🚀🔥