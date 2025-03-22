import gradio as gr
import random

# Simulated AI responses for different functionalities
def respond(message, history, system_message, max_tokens, temperature, top_p):
    flight_responses = [
        "Your flight from New York to London is confirmed. Departure: 10:30 AM, Terminal 3.",
        "Real-time tracking: Flight AI-203 is on schedule, estimated arrival in 2 hours.",
        "No security threats detected. All systems operational.",
        "Your booking for Flight QR-789 is successful. Seat: 12A, Gate: B5.",
        "ALERT: Unusual activity detected. Security teams have been notified.",
    ]

    security_responses = [
        "System scan complete: No hijacking threats detected.",
        "AI surveillance detected a minor anomaly, monitoring in progress.",
        "Security breach attempt blocked successfully. Your data is safe.",
    ]

    chatbot_responses = [
        "How can I assist you with your flight booking today?",
        "Would you like to check your flight status or security updates?",
        "Welcome to Skyparadise AI! Your safety is our priority.",
    ]

    # Simulating interactive responses
    if "flight" in message.lower():
        response = random.choice(flight_responses)
    elif "security" in message.lower() or "hijack" in message.lower():
        response = random.choice(security_responses)
    else:
        response = random.choice(chatbot_responses)

    return response

# Customized AI Chat for Skyparadise Services
demo = gr.ChatInterface(
    respond,
    title="Skyparadise: AI-Powered Flight Services ✈️",
    description="🚀 Secure, hijack-free AI assistance for flights, bookings, and real-time tracking.",
    additional_inputs=[
        gr.Textbox(value="You are an AI assistant for secure flight services.", label="System message"),
        gr.Slider(minimum=32, maximum=2048, value=512, step=1, label="Max Tokens"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.95, step=0.05, label="Top-p"),
    ],
    theme="soft",
)

if __name__ == "__main__":
    demo.launch()
