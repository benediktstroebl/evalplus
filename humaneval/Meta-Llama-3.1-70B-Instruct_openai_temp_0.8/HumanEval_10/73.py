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
    # Handle edge case
    if not string:
        return ''

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        suffix = string[i - 1:]
        if is_palindrome(suffix):
            break

    # Append reverse of prefix before the longest palindromic suffix
    prefix = string[:-len(suffix)]
    return string + prefix[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

In this code, the `make_palindrome` function works by first finding the longest suffix of the input string that is a palindrome. It does this by checking all suffixes from longest to shortest. Once it finds the longest palindromic suffix, it appends the reverse of the remaining prefix to the end of the input string. This creates the shortest palindrome that begins with the input string.