```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    Algorithm idea simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Returns: The value of the shortest palindrome that begins with the given string.

    Returns: value of the shortest palindrome with the original string.

    Test cases:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    >>> make_palindrome('racecar')
    'racecar'
    """
```