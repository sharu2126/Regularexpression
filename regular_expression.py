##1. Extract All Email Addresses from a String
##Problem Statement: Write a function that extracts all email addresses from a given string.
##Hint:
##• Use regular expressions to identify patterns that start with alphanumeric characters, followed by @, then a domain name with a period, and finally a valid domain extension.
##Input Example:
##text = "Contact john.doe@example.com, jane_doe123@domain.org for more details."
##Output Example:
##['john.doe@example.com', 'jane_doe123@domain.org']
##

##import re
##text="Contact john.doe@example.com, jane_doe123@domain.org for more details."
##logic=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
##match=re.findall(logic,text)
##print(match)

##2. Check if a String is a Valid Phone Number
##Problem Statement: Write a function to check whether a given string is a valid phone number in the format (XXX) XXX-XXXX.
##Hint:
##•   Use the regular expression pattern \(\d{3}\) \d{3}-\d{4} to match the phone number.
##Input Example:
##phone = "(123) 456-7890"
##Output Example:
##True
##Input Example:
##phone = "123-456-7890"
##Output Example:
##False

##import re
##
##def phone_no(phone:str)->bool:
##    logic= r'^\(\d{3}\) \d{3}-\d{4}$' 
##    return bool(re.match(logic,phone))
##print(phone_no("(123) 456-7890"))
##print(phone_no("123-456-7890"))



##3. Count the Number of Words in a String
##Problem Statement: Write a function that counts the number of words in a given string. Words are defined as sequences of alphanumeric characters separated by spaces or punctuation.
##Hint:
##•	You can use the regular expression \w+ to match words.
##Input Example:
##text = "Hello, my name is John Doe."
##Output Example:
##5

##import re
##text="Hello, my name is John Doe."
##logic=r'\s'
##match=re.findall(logic,text)
##print(len(match))




##4. Validate a URL
##Problem Statement: Write a function to validate if a given URL is in the format http:// or https:// followed by a valid domain name and an optional path.
##Hint:
##•	A URL pattern can be described as https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?.
##Input Example:
##url = "https://www.example.com/path/to/page"
##Output Example:
##True
##Input Example:
##url = "ftp://example.com"
##Output Example:
##False


##import re
##def URL(url:str)->bool:
##    logic=r'https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?'
##    return bool(re.match(logic,url))
##print(URL("https://www.example.com/path/to/page"))
##print(URL("ftp://example.com"))
##print(URL("https://www.amzon.com"))



##5. Extract Dates from a String
##Problem Statement: Write a function to extract all dates in the format MM-DD-YYYY from a given string.
##Hint:
##•	Use the regular expression \b\d{2}-\d{2}-\d{4}\b to match dates.
##Input Example:
##text = "My birthday is on 12-10-1995 and my friend's birthday is 01-20-1990."
##Output Example:
##['12-10-1995', '01-20-1990']


##import re
##logic=r'\b\d{2}-\d{2}-\d{4}\b'
##text = "My birthday is on 12-10-1995 and my friend's birthday is 01-20-1990."
##match=re.findall(logic,text)
##print(match)


##6. Replace All Whitespace with a Single Space
##Problem Statement: Write a function that replaces all consecutive whitespace characters (spaces, tabs, newlines) in a string with a single space.
##Hint:
##•	Use \s+ to match one or more whitespace characters and replace them with a single space.
##Input Example:
##text = "This    is    a   test  string.     "
##Output Example:
##"This is a test string."

##import re
##def whitespace(text:str)->str:
##    return re.sub(r'\s+' ,' ',text).strip()
##
##text = "This    is    a   test  string.     "
##print(whitespace(text))


##7. Extract All Hashtags from a Text
##Problem Statement: Write a function to extract all hashtags (words starting with #) from a given string.
##Hint:
##•	Use the regular expression #\w+ to match hashtags.
##Input Example:
##text = "Loving the weather today! #sunny #goodvibes #relax"
##Output Example:
##['#sunny', '#goodvibes', '#relax']


##import re
##logic=r'#\w+'
##text="Loving the weather today! #sunny #goodvibes #relax"
##match=re.findall(logic,text)
##print(match)

##8. Validate a Strong Password
##Problem Statement: Write a function to validate a password. A strong password must meet the following criteria:
##•	Be at least 8 characters long.
##•	Contain both uppercase and lowercase letters.
##•	Contain at least one digit.
##•	Contain at least one special character (e.g., @, #, $).
##Hint:
##•	Use the regular expression ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$.
##Input Example:
##password = "Strong@123"
##Output Example:
##True
##Input Example:
##python
##Copy
##password = "weakpass"
##Output Example:
##False


##import re
##def password(passwd:str)->bool:
##    logic=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
##    return bool(re.match(logic,passwd))
##print(password("Strong@123"))
##print(password("weakpass"))
##print(password("Ysm@1234"))


##9. Find All IP Addresses in a String
##Problem Statement: Write a function to extract all valid IPv4 addresses from a given string. An IPv4 address has the form X.X.X.X, where X is a number between 0 and 255.
##Hint:
##•	Use the pattern (?:\d{1,3}\.){3}\d{1,3} to match IP addresses and validate that each part is between 0 and 255.
##
##Input Example:
##text = "The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."
##Output Example:
##['192.168.0.1', '10.0.0.255']



##import re
##logic=r'\b(?:\d{1,3}\.){3}\d{1,3}\b' 
##text="The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."
##match=re.findall(logic,text)
##print(match)


##10. Validate a Date in DD-MM-YYYY Format
##Problem Statement: Write a function to validate if a given string represents a valid date in the format DD-MM-YYYY.
##Hint:
##•	Use the regular expression ^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$ to match the format, then use Python’s datetime module to validate the actual date.
##Input Example:
##date = "15-04-2023"
##Output Example:
##True
##Input Example:
##date = "31-02-2023"
##Output Example:
##False

##import re
##def dateformat(date:str)->bool:
##    logic=r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$'
##    return bool(re.match(logic,date))
##print(dateformat("15-04-2023"))





                                                             


