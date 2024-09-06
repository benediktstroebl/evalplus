```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    if string == "" or len(string) == 1:
        return ""
    
    palindrome = ""
    while True:
        palindrome += string[-1]
        string = string[:0] + string[-1:]
        if string == "" or len(string) == 1:
            break
    
    return palindrome[::-1] + palindrome
```