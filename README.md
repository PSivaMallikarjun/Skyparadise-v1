# Skyparadise-v1

## Overview

Skyparadise-v1 is a Small Language Model (SLM)-powered chatbot designed to provide intelligent conversational responses with minimal computational overhead. This chatbot leverages lightweight AI models to ensure efficient and fast interactions while maintaining a high level of user engagement.

## Features

- **Small Language Model (SLM):** Optimized for low latency and efficiency.
- **Conversational AI:** Provides meaningful and context-aware responses.
- **Lightweight & Scalable:** Suitable for deployment on edge devices and low-power systems.
- **Customizable Responses:** Adaptable to specific domains and applications.
- **Multi-Platform Support:** Can be integrated into web, mobile, and desktop applications.

## Installation

### Requirements

Ensure you have the following dependencies installed:

```
pip install gradio torch transformers
```

### Running the Chatbot

To launch Skyparadise-v1, run the following command:

```
python skyparadise_chatbot.py
```

## Usage

1. Start the chatbot using the above command.
2. Type a message into the input field.
3. Receive an AI-generated response based on the input context.

## API Integration

Skyparadise-v1 can be integrated into various applications via an API. Example usage:

```python
import requests

response = requests.post("http://localhost:8000/chat", json={"message": "Hello!"})
print(response.json())
```

## Deployment

The chatbot can be deployed on cloud platforms like AWS, Azure, or Google Cloud.
For containerized deployment, use Docker:

```sh
docker build -t skyparadise-chatbot .
docker run -p 8000:8000 skyparadise-chatbot
```

## License

Skyparadise-v1 is released under the MIT License. You are free to use, modify, and distribute this software with proper attribution.

## Contributors

- **Developer:** Siva Mallikarjun Parvatham
![Screenshot 2025-03-22 191209](https://github.com/user-attachments/assets/a6c1f744-51e6-440d-a6a8-b94705da039b)
![Screenshot 2025-03-22 191322](https://github.com/user-attachments/assets/d72af37e-ce18-4ae7-8862-19ad79a29b8a)
![Screenshot 2025-03-22 191331](https://github.com/user-attachments/assets/32b88bb3-1d9b-4d37-8893-37fa53b3dab5)
![Screenshot 2025-03-22 191420](https://github.com/user-attachments/assets/20f6e236-2ba8-478b-96bc-466388385330)





For contributions, submit a pull request to the official repository.


