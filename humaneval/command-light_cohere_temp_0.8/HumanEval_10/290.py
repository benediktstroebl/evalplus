Here's the Python script with the self-contained function:
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
        if string[1:] == string[::-1]:
            break
        string = string[1:] + string[0]
    return palindrome[::-1]
```
The function `is_palindrome` checks if the given string is a palindrome. The function `make_palindrome` then generates the shortest palindrome that begins with the given string.