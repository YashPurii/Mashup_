from flask import Flask, request, render_template
import smtplib
import shutil
import os
from zipfile import ZipFile
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import shutil
import os
from zipfile import ZipFile
import smtplib

backend = Flask(__name__)


@backend.route("/", methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        artist = request.form["arg1"]  # artist name
        num_vid = request.form["arg2"]  # num of videos
        dur = request.form["arg3"]  # duration
        email = request.form["arg4"]  # email_ID

        out_file = "mashup.mp3"
        result = run_script(artist, num_vid, dur, out_file, email)

        return result

    return render_template("index1.html")


# def sendMail(eID, body_mail):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('fsharma_be20@thapar.edu', 'hzbtjgxysrrgznud')
#     server.sendmail('fsharma_be20@thapar.edu', eID, body_mail)
#     server.close()


def run_script(arg1, arg2, arg3, arg4, email):
    import subprocess
    command = ["python", "script.py", arg1, arg2, arg3, arg4]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # path = str(os.getcwd())
    # path = path + "\\"

    # msg = MIMEMultipart()
    # body_part = MIMEText("mashup created at", 'plain')
    # msg['Subject'] = "Mashup created at ["
    # # msg['From'] = EMAIL_FROM
    # msg['To'] = email

    # msg.attach(body_part)

    # path = str(os.getcwd())
    # path = path + "\\"
    # with open(path+"mashup.zip",'rb') as file:
    #     msg.attach(MIMEApplication(file.read(), Name='mashup.zip'))
    #     sendMail(email, msg.as_string())

    return result.stdout.decode()


if __name__ == "__main__":
    
    backend = Flask(__name__)
    backend.debug = True
    backend.run()
