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

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            return string + string[:i-1][::-1]


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
```

This script first checks if the input string is empty. If it is, it returns an empty string. Otherwise, it iterates over the length of the string in a descending order. For each length, it checks if the string's suffix of the given length is a palindrome. If it is, it appends the reverse of the string's prefix to the end of the original string and returns the resulting palindrome.