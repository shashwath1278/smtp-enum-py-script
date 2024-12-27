import smtplib

def smtp_enum(target, wordlist):
    with open(wordlist, 'r') as f:
        for uname in f:
            uname = uname.strip()  
            server = smtplib.SMTP(target, 25)  
            server.ehlo()  
            code, response = server.docmd("VRFY", uname) 
            print("Response for %s: %s" % (uname, response.decode()))  
            server.quit()

target = input("target ip or hostname: ")
wordlist = input("format: wordlist.txt (assuming wordlist is in same dir as the script): ")

smtp_enum(target, wordlist)
