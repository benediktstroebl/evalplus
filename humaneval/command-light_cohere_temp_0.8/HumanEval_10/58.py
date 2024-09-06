```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ""
    palindrome = ""
    while True:
        palindrome += string[0]
        string = string[1:]
        if not string: 
            break
    return palindrome[::-1] + palindrome
``` 
Do you need help with anything else with code implementation or any other topic?