```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def longest_palindromic_suffix(string: str) -> str:
    """ Find the longest palindromic suffix of a string """
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            return string[i-1:]


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
    palindromic_suffix = longest_palindromic_suffix(string)
    return string + palindromic_suffix[::-1]


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first defines a helper function `longest_palindromic_suffix` to find the longest palindromic suffix of a string. The `make_palindrome` function then uses this helper function to find the longest palindromic suffix and appends the reverse of the prefix to the end of the string to create the shortest palindrome that begins with the supplied string.