mail_address = input("Enter your mail address => ")
if('@' in mail_address):
    index = mail_address.index('@')
    print("Name : ",mail_address[:index])
    print("Domain name : ",mail_address[index+1:])
else:
    print("Enter a valid email address")
