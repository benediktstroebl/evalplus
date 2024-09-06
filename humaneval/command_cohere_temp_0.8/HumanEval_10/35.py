Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Find the longest string prefix that precedes the palindromic suffix.
    j = 0
    while not is_palindrome(string[:i][::-1] + string[j:i]):
        j += 1

    return make_palindrome(string[:j] + string[i:][::-1] + string[j:i])
```

This code defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the supplied string. It uses two pointers to efficiently find the shortest palindrome. The `is_palindrome` function is reused from the original prompt.

The script can be tested on the following examples:
```python
>>> make_palindrome('')
''
>>> make_palindrome('cat')
'catac'
>>> make_palindrome('cata')
'catac'
```