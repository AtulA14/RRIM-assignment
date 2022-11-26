import re
def isValid(s):
    Pattern = re.compile("^\+?[0-9]{0,1}?[-\s]?\(?[0-9]{3}?\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$")
    return Pattern.match(s)
s = input("Enter a number:")
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")





