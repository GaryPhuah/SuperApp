# SuperApp

**SuperApp** is a Python-based tool that demonstrates how to run a Python script for accessing certain video platforms. It can optionally be packaged into a standalone executable using [PyInstaller](https://www.pyinstaller.org/).

> **Inspired by [琥珀君](https://www.cnblogs.com/eliteboy/p/19013379)** – all credit for the original idea and method goes to them.


---

## Features

- Runs directly via Python (`python VIPmovie.py`)
- Optional: build as an `.exe` using PyInstaller
- Simple and lightweight project structure

---

## Prerequisites

To run this app, you’ll need:

- Python 3.8 or higher
- `pip` (Python package manager)
- A code editor (VS Code, PyCharm, etc.)

---

## Installation & Setup

### 1. Install Python

Download from the [official Python website](https://www.python.org/downloads/).  
☑️ During setup, make sure to select **“Add Python to PATH”**.

### 2. Clone This Repository

```bash
git clone https://github.com/GaryPhuah/SuperApp.git
cd SuperApp
```

---

## Running the Application

Run the app directly using Python:

```bash
python VIPMovie/VIPmovie.py
```

No need to compile or build anything.

---

### 1. Install PyInstaller

```bash
pip install pyinstaller
```
---


## Project Structure

```
SuperApp/
├── MovieVIP.iml      # (PyCharm config, ignore)
├── VIPmovie.py       # ← Main script
└── README.md
└── DemoResult.png
```

---

## Acknowledgements

- Inspired by **琥珀君**
- Built using Python

---

## ⚠️ Disclaimer

This project is intended for **educational use only**.  
Please respect the terms of use of any third-party platforms involved.

---
## 🖼️ Demo

Here's a quick preview of the result when running the script:

![Demo Result](DemoResult.png)
