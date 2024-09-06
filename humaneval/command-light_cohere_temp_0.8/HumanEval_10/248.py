Here is a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    # Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    return ''.join(reversed(prefix)) + suffix
```

This function takes a string as input and returns a boolean indicating whether the string is a palindrome, and a string that is the shortest palindrome that begins with the original string.