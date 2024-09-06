Here is a Python script that contains a self-contained function that solves the problem of making a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""

    palindrome = []
    i = 0
    while i < len(string):
        if is_palindrome(string[i:]):
            palindrome.append(string[i:])
        i += 1
    return ''.join(palindrome[::-1])
```
The function is_palindrome returns True if the string is a palindrome, and False otherwise. The function make_palindrome takes a string as input and returns the shortest palindrom that begins with the given string.