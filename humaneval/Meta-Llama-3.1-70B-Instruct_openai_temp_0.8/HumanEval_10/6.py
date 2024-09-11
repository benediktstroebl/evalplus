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
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), 0, -1):  # find longest postfix that is a palindrome
        if is_palindrome(string[-i:]):
            postfix = string[-i:]
            prefix = string[:-i]
            return string + prefix[::-1]  # append reverse of prefix to string


# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script uses two functions, `is_palindrome` and `make_palindrome`. `is_palindrome` checks whether a given string is a palindrome by comparing the string to its reverse. `make_palindrome` uses this helper function to find the longest postfix of the input string that is a palindrome, then appends the reverse of the prefix that comes before this postfix to the input string.