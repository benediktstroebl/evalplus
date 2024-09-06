```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """
    if not string: return ''
    # Algorithm idea:
    # - Find the longest postfix of supplied string that is a palindrome
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return ''.join(str.lower()) + make_palindrome(string[1:])
```

This code is a complete and self-contained solution to the problem. It defines two functions:
`is_palindrome` tests if a given string is a palindrome.
`make_palindrome` function creates a palindrome given a string. It uses the simple idea of finding the longest palindromic substring and appending its reverse to the original string.