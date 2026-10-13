# Simple API Client Using Python

## 1. Objective
Develop a Python program that connects to a public REST API, retrieves JSON data, processes the response, and displays selected information in a readable format.

## 2. Technologies Used
- Python
- Requests library
- REST API
- JSON
- Visual Studio Code

## 3. Features
- Fetches data from a public REST API.
- Processes JSON responses.
- Displays post ID, user ID, title, and body.
- Handles connection errors, timeouts, and HTTP errors.
- Uses a timeout to avoid waiting indefinitely.

## 4. API Used
URL: https://jsonplaceholder.typicode.com/posts/1

This public API provides sample post data and does not require an API key.

## 5. Installation
Install the required Requests library:

bash
python -m pip install requests


If using a virtual environment on Windows, run:

powershell
.\.venv\Scripts\python.exe -m pip install requests


## 6. How to Run
1. Save the Python program as api_client.py.
2. Open the project folder in VS Code.
3. Open Terminal → New Terminal.
4. Install the Requests library.
5. Run the program:

powershell
.\.venv\Scripts\python.exe api_client.py


## 7. Expected Output
The program displays:
- Post ID
- User ID
- Post title
- Post body

It also displays a success message when the API request succeeds.

## 8. Error Handling
The program handles:
- Connection errors
- Request timeouts
- HTTP errors
- Other request-related errors
- Invalid JSON responses

## 9. Conclusion
This project demonstrates how to make API requests using Python, process JSON data, display results, and handle common network errors