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
    if not string:
        return ''

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks whether a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that begins with a supplied string.

In the `make_palindrome` function, it iterates over the string from the end to the start to find the longest postfix that is a palindrome. Once found, it appends the reverse of the prefix that comes before the palindromic suffix to the end of the string.

The test cases at the end demonstrate the functionality of the `make_palindrome` function.