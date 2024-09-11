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
    # Find the longest postfix of supplied string that is a palindrome
    for length in range(1, len(string) + 1):
        if is_palindrome(string[-length:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[-length:][::-1]

    return string


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
```

This script implements the `make_palindrome` function by utilizing the `is_palindrome` helper function to find the longest postfix of the input string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix.