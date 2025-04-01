import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendMail(receiver_email,IssueTotal,IssuePending,IssueResolved):

    sender_email = "akashjajee81@gmail.com"
    password = "utcybzhhzylqsctg"
    # Recipient's email
    #receiver_email = "akash.jajee@healthgraph.in"

    # Set up the SMTP server (Gmail in this case)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port for sending email over TLS

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Issue Reported details from Python"

    # Email body
    body = f"Dear Customer\nPlease Find the Details of the issue reported by you during This Month,\n\nTotal Issues Reported : {IssueTotal}.\nTotal Issues Pending :  {IssuePending} \nTotal Issues Resolved :  {IssueResolved}\n\n\nThanks"

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the Gmail SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log in to the email account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        server.quit()  # Close the server connection


