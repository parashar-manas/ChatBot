<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hostel Assistant Chatbot</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #fef6f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .chat-container {
            width: 400px;
            max-width: 90%;
            background-color: #ffffff;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .chat-header {
            background-color: #ffd6d6;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.2em;
        }

        .chat-messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .message {
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 80%;
            word-wrap: break-word;
        }

        .user-msg {
            align-self: flex-end;
            background-color: #c6f6d5;
        }

        .bot-msg {
            align-self: flex-start;
            background-color: #fce1f0;
        }

        .chat-input {
            display: flex;
            padding: 10px;
            border-top: 1px solid #ddd;
            background-color: #fff5f5;
        }

        .chat-input input {
            flex: 1;
            padding: 10px 15px;
            border-radius: 20px;
            border: 1px solid #ddd;
            outline: none;
        }

        .chat-input button {
            padding: 10px 15px;
            margin-left: 10px;
            border: none;
            border-radius: 20px;
            background-color: #ffd6d6;
            cursor: pointer;
            font-weight: bold;
        }

        .chat-input button:hover {
            background-color: #ffb3b3;
        }

        /* Scrollbar styling */
        .chat-messages::-webkit-scrollbar {
            width: 6px;
        }
        .chat-messages::-webkit-scrollbar-thumb {
            background-color: #ffc1c1;
            border-radius: 3px;
        }
    </style>
</head>
<body>

<div class="chat-container">
    <div class="chat-header">🏡 Hostel Assistant</div>
    <div class="chat-messages" id="chatMessages"></div>
    <div class="chat-input">
        <input type="text" id="userInput" placeholder="Ask me anything...">
        <button onclick="sendMessage()">Send</button>
    </div>
</div>

<script>
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage(message, 'user-msg');
        userInput.value = '';

        try {
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            const data = await res.json();
            appendMessage(data.answer, 'bot-msg');
        } catch (err) {
            appendMessage('Sorry, there was an error. Try again later.', 'bot-msg');
        }

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function appendMessage(text, className) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${className}`;
        msgDiv.textContent = text;
        chatMessages.appendChild(msgDiv);
    }

    // Allow Enter key to send message
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
</script>

</body>
</html>
