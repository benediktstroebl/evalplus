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
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Find the palindromic prefix, which is the reverse of the remaining part
            prefix = string[:-i][::-1]
            return string + prefix

    # If no palindrome found, return the original string
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `make_palindrome` function, which finds the shortest palindrome that begins with a given string. It does this by finding the longest palindromic suffix of the string and appending to it the reverse of the remaining prefix. If no palindromic suffix is found, it returns the original string. The `is_palindrome` function is used to check if a string is a palindrome. The script also includes test cases to verify its correctness.