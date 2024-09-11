```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string

    rev_string = string[::-1]
    for i in range(len(string)):
        if is_palindrome(rev_string[i:]):
            return string + rev_string[:i]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

This Python script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks whether a given string is a palindrome by comparing it to its reverse. The `make_palindrome` function generates the shortest palindrome that begins with a supplied string. It first checks if the input string is already a palindrome. If not, it finds the longest postfix of the string that is a palindrome and appends the reverse of the remaining prefix to the end of the string.