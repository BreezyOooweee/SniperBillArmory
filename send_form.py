from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Email settings
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use an app password, not your main one
RECEIVER_EMAIL = "bryanstring24@email.com"

@app.route('/')
def index():
    # Optional: render your HTML file if you move it into a templates folder
    return render_template_string("<h1>Go to /appointments.html</h1>")

@app.route('/send', methods=['POST'])
def send_email():
    # Collect form data
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    time = request.form.get('time')
    services = request.form.get('services')

    # Construct the message
    msg = EmailMessage()
    msg['Subject'] = f"New Appointment: {fname} {lname}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    msg.set_content(f"""
    New appointment request:

    Name: {fname} {lname}
    Email: {email}
    Phone: {phone}
    Service: {services}
    Date: {date}
    Time: {time}
    """)

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        return "✅ Appointment request sent successfully!"
    except Exception as e:
        print("Error:", e)
        return "❌ Failed to send appointment request."

if __name__ == '__main__':
    app.run(debug=True)
