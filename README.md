# 🐱 FastAPI Cat Fact Profile API

A simple and elegant **FastAPI** application that returns your **profile information** along with a **random cat fact** fetched from the public [Cat Facts API](https://catfact.ninja/fact).

---

## 📘 **Project Description**

This RESTful API exposes a single **GET** endpoint at `/me`.
When called, it returns:

* ✅ A **success message**
* ✅ Your **user details** (email, name, backend stack)
* ✅ A **current UTC timestamp** (ISO 8601 format)
* ✅ A **random cat fact** retrieved dynamically from the Cat Facts API

If the external API fails, the app handles it gracefully and still returns a valid JSON response with a fallback message.

---

## 🧩 **Code Overview**

### Main components (`app.py`)

| Section                   | Description                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Logging Configuration** | Uses Python’s built-in `logging` to log important app events to both console and file (`app.log`). |
| **User Info**             | Static dictionary (`USER_INFO`) with email, full name, and stack.                                  |
| **External API Call**     | Fetches a random cat fact from `https://catfact.ninja/fact` using `httpx.AsyncClient`.             |
| **Error Handling**        | Gracefully catches API/network errors and returns a fallback message.                              |
| **Timestamp**             | Returns the current UTC time in ISO 8601 format.                                                   |

---

## ⚙️ **How It Works (Process Description)**

1. When a **GET request** is made to `/me`:

   * The app logs the incoming request.
   * It fetches a random cat fact from the Cat Facts API.
   * It records the current UTC timestamp.
   * It constructs a JSON response with your user info, timestamp, and the cat fact.
   * It logs a success message and returns the response.

2. If the Cat Facts API fails or times out:

   * The error is logged.
   * A fallback message is returned in place of the cat fact.
   * The endpoint still responds with `"status": "success"` (graceful degradation).

---

## 💻 **Installation and Running Locally**

Follow these steps to run the project **without Docker**, using only Python.

### 🪶 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-catfact-api.git
cd fastapi-catfact-api
```

### 📦 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 📜 3. Install Dependencies

Make sure you have a `requirements.txt` file that includes:

```
fastapi==0.119.0
uvicorn==0.35.0
httpx==0.28.1
```

Then install:

```bash
pip install -r requirements.txt
```

### 🚀 4. Run the App

```bash
uvicorn app:app --reload
```

The app will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 **Calling the GET Endpoint**

You can call the endpoint in any of the following ways:

### Using `curl`

```bash
curl http://127.0.0.1:8000/me
```

### Using a Browser

Visit:

```
http://127.0.0.1:8000/me
```

### Using Python

```python
import requests

response = requests.get("http://127.0.0.1:8000/me")
print(response.json())
```

---

## ✅ **Example Successful Responses**

### Example 1

```json
{
  "status": "success",
  "user": {
    "email": "nbinael@yahoo.com",
    "name": "Binael Nchekwube",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T21:25:45.763423+00:00",
  "fact": "Cats sleep for 70% of their lives."
}
```

### Example 2

```json
{
  "status": "success",
  "user": {
    "email": "nbinael@yahoo.com",
    "name": "Binael Nchekwube",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T21:30:02.123456+00:00",
  "fact": "A cat’s whiskers are roughly as wide as its body."
}
```

---

## ⚠️ **Example Response When External API Fails**

If the Cat Facts API is unavailable or times out, the response will look like this:

```json
{
  "status": "success",
  "user": {
    "email": "nbinael@yahoo.com",
    "name": "Binael Nchekwube",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T21:32:10.987654+00:00",
  "fact": "Could not fetch cat fact at the moment. Try again later."
}
```

---

## 🧠 **Key Features**

* 🚀 Lightweight, async-ready FastAPI app
* 🐱 Live integration with [Cat Facts API](https://catfact.ninja/fact)
* 🧾 Real-time UTC timestamp (ISO 8601 format)
* ⚙️ Built-in logging (console + file)
* 🛡️ Graceful failure handling

---

## 🪵 **Logs**

All app activity is logged in two places:

* `app.log` — file-based log for persistent tracking
* Console output — visible in terminal or Railway logs

Example:

```
2025-10-19 21:20:45,120 - [INFO] - Received request to /me endpoint
2025-10-19 21:20:45,121 - [INFO] - Fetching cat fact from https://catfact.ninja/fact
2025-10-19 21:20:45,302 - [INFO] - Successfully fetched cat fact
2025-10-19 21:20:45,303 - [INFO] - Returning /me response successfully
```

---

## 👨‍💻 **Author**

**Binael Nchekwube**
📧 Email: [nbinael@yahoo.com](mailto:nbinael@yahoo.com)
💻 Stack: Python / FastAPI

---

Would you like me to format this `README.md` for **GitHub markdown** (with badges and table of contents at the top)? It’ll look great on your public repository.
