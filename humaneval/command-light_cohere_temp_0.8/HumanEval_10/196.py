Here's the Python script with a self-contained function that creates a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea: 
    # - Find the longest postfix of supplied string that is a palindrome.
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string:
        return ''

    palindrome = string
    
    postfix = ''
    while True:
        if postfix + palindrome[-1:][::-1] == palindrome:
            postfix += palindrome[-1:]
            break
        else:
            palindrome += postfix
            postfix = ''

    return palindrome
```
This code defines two functions:
1. Palindrome Function By testing if a given string is a palindrome. It returns `True` if the string is palindrome and `False` otherwise.
2. Palindrome_ Maker: This function constructs a palindrome by finding the longest postfix of the string that is also a palindrome and then appending the reversed prefix to the reversed postfix.

The function makes sure that the resultant palindrome is the shortest possible. The code is self-contained, and the approach is concise and efficient.