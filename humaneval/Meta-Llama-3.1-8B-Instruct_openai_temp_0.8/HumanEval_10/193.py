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
    # Find the longest palindrome suffix
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Find the prefix that comes before the palindromic suffix
            prefix = string[:-i]
            # Append the reverse of the prefix to the end of the string
            palindrome = string + prefix[::-1]
            return palindrome

    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script uses a simple approach to find the longest palindrome suffix of the input string, and then appends the reverse of the prefix that comes before the palindromic suffix to the end of the string to form the shortest palindrome that begins with the input string.