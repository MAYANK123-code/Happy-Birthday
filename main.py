import pandas as pd
import datetime
import smtplib
#df = pd.read_excel("data.xlsx")
#print(df)

#enter your authetication details
GMAIL_ID = 'username@gmail.com'
PASSWORD = 'your password'

def fun(to, sub, msg):
    print("Email to "+to+" sent with a subject "+sub+" and message "+msg)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, PASSWORD)

    s.sendmail(GMAIL_ID, to, msg=msg)
    s.quit()
    
    pass

if __name__ == "__main__":
    #fun(GMAIL_ID, "subject", "test message")
    
    df = pd.read_excel("data.xlsx")
    #print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    #print(today)
    
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        #print(bday)
        if(bday==today):

            fun(to=item['Email'], sub="Birthday wish", msg=item['Dialogue'])
