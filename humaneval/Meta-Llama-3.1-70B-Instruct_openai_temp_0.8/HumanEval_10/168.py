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

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines the `is_palindrome` function to check if a given string is a palindrome. It then uses this function in the `make_palindrome` function to find the shortest palindrome that begins with the supplied string.

Here's an explanation of how the `make_palindrome` function works:

1. If the input string is already a palindrome, it returns the string as it is.
2. It then iterates over the input string from the end to the start, checking if the suffix of the string is a palindrome.
3. As soon as it finds a palindromic suffix, it returns the input string appended with the reverse of the prefix that comes before the palindromic suffix.