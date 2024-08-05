import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

my_email = "ses-smtp-user.20204084-114029"
password = "BG4MJ9PS6tOP+GpbSsuGn/DAu6H3aFXrWfvMB0VT4sK4"

# Read email addresses from an external file
with open('emails.txt', 'r') as file:
    email_list = [line.strip() for line in file]

# Read the PDF file
pdf_filename = 'b.pdf'
with open(pdf_filename, 'rb') as pdf_file:
    pdf_data = pdf_file.read()

# Establish SMTP connection
with smtplib.SMTP("smtp.yousmtp.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    with open('sent_emails.txt', 'a') as sent_file:
        for email in email_list:
            # Create a MIME message
            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = email
            msg['Subject'] = "Reference No. 143737 has been provided to you with your item. 2OAUMMIAOOM of item"

            # Attach the body text
            body = MIMEText("Do not hesitate to contact our customer support staff if you need further help or if you have any questions. We can be contacted by phone at [Customer Support Phone Number] or by email at [Customer Support Email]. We are available to assist you with any questions or issues that you may have.")
            msg.attach(body)

            # Attach the PDF file
            attachment = MIMEApplication(pdf_data, _subtype="pdf")
            attachment.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
            msg.attach(attachment)

            # Send the email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=msg.as_string()
            )
            sent_file.write(email + '\n')