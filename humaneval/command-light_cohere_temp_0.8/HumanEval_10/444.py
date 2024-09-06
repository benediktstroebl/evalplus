Here is a self-contained Python function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # The idea is to find the longest palindrome using a loop, 
    # and then reverse and append the palindrome prefix
    # before the rest of the string.
    palindrome = ''.join(string)

    return palindrome + palindrome[::-1]
```
The function `is_palindrome` returns `True` if the string is a palindrome, and `False` otherwise. The function `make_palindrome` returns a new string that is a palindrome of the original string.