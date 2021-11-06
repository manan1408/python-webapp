import smtplib  # python library to send emails

recipient = input("Enter Email of the Recipient:\n") #receives mail address

message = input("Enter the content of the mail:\n")  #message to be send


def SendEmail(recipient , message):
    server = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 = port number
    server.ehlo() # check the smtp connection 
    server.starttls()  # start the conection 
    server.login("SenderEmail@gmail.com" , "SendersEmailPassword")  
    server.sendmail("senderEmail@gmail.com" , recipient , message)
    server.close() 
    

SendEmail(recipient , message)  
