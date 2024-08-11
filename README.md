# BeeGPT - OpenAI-Based Chatbot for Beekeepers

BeeGPT is a specialized AI-powered chatbot designed to assist beekeepers with various aspects of beekeeping. Built on OpenAI's GPT model, this chatbot provides informative and helpful responses to questions about beekeeping, hive management, and bee health. This project uses Flask as the web framework, and it integrates with OpenAI's API to deliver a seamless user experience.

## Features

- **Interactive Chat Interface**: Ask questions about beekeeping and receive detailed responses from the BeeGPT chatbot.
- **Custom Themed UI**: A visually appealing dark-themed interface with custom icons and cursors, tailored for the beekeeping community.
- **Audio Integration**: Background music and sound effects enhance the user experience.
- **SSL Certificate Handling**: Custom SSL handling is implemented to ensure secure API requests.

## Prerequisites

- Python 3.x
- Flask
- OpenAI API Key
- Requests library
- Python-dotenv

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/BeeGPT.git
   cd BeeGPT

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Python Packages**
pip install -r requirements.txt

4. **Set Up the Environment Variables**
Create a .env file in the root directory of your project:
    ```bash
    Code kopieren
    touch .env

5. **Run the Application**

    ```bash
    Code kopieren
    python app.py

The application will start on http://127.0.0.1:5000/.

## Usage

### Access the Chatbot

Open your web browser and navigate to `http://127.0.0.1:5000/`.

### Interact with the Chatbot

1. Type your question or message about beekeeping in the textarea.
2. Click the "Sting!" button to submit your query.
3. The chatbot will respond with information related to your query.

### Background Music

Click the "Music On" button to start the background music.

## File Structure

- **`app.py`**: Main application script containing Flask routes and OpenAI API integration.
- **`templates/index.html`**: HTML template for the chatbot interface.
- **`static/`**: Directory containing static assets like images and audio files.
  - **`pictures/`**: Directory for images (e.g., bee icon, custom cursor).
  - **`audio/`**: Directory for audio files (e.g., background music, click sound).
- **`.env`**: Environment variables file for storing sensitive information (not included in version control).

## Troubleshooting

- **No Response Displayed**: Ensure that the Flask application is correctly passing `chatgpt_response` and `error_message` to the template. Check the network tab in the browser's developer tools for any errors.
- **SSL Errors**: Ensure that your OpenAI API key is correctly set in the `.env` file and that your network allows secure connections.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you have suggestions for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
