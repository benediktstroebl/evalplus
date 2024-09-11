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
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first defines a helper function `is_palindrome` to check if a given string is a palindrome. The `make_palindrome` function iterates through the input string from the end to the beginning, checking for the longest palindromic postfix. Once found, it appends the reverse of the prefix that comes before the palindromic suffix to the end of the string, resulting in the shortest palindrome that begins with the supplied string.