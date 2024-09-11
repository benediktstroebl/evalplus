```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

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
    if not string:
        return ''

    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

The `make_palindrome` function iterates over the input string from the end to the start. For each postfix of the string, it checks if the postfix is a palindrome using the `is_palindrome` function. If a palindromic postfix is found, the function appends the reverse of the corresponding prefix to the end of the string to form the shortest palindrome.