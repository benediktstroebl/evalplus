Here is a Python script that contains a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    if string == """:
        return ""
    elif string[-1] == "-":
        return make_palindrome(-string[:-2]) + string[-1:]
    else:
        return make_palindrome(string[:-2]) + string[-1:]
```
This script provides a function `is_palindrome` that checks if a given string is a palindrome and another function `make_palindrome` that constructs a palindrome from a given string.