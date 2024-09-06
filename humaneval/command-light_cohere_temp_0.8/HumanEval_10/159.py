```python
def is_palindrome(string):
    """ Returns True if the string is a palindrome, False otherwise """
    return string == string[::-1]

def make_palindrome(string):
    """ Returns the shortest palindrome that begins with the supplied string """
    if not string:
        return ''

    palindrome = string[:0:-1] + string[::-1]
    return palindrome
```
This script provides a function that checks whether a given string is a palindrome and another function that constructs the shortest palindrome that begins with a given string.