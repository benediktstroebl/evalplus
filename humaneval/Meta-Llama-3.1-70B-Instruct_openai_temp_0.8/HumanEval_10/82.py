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

    # Find the longest prefix that is a palindrome
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        if is_palindrome(prefix):
            # The rest of the string needs to be mirrored
            suffix = string[i:]
            return string + suffix[::-1]

    # If no prefix is a palindrome, the whole string needs to be mirrored
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
The `is_palindrome` function checks if a given string is the same forwards and backwards.

The `make_palindrome` function works by finding the longest prefix of the string that is a palindrome. It then appends the reverse of the remaining suffix to the end of the string to create the shortest palindrome.

Note that the `make_palindrome` function handles the case where the input string is empty, in which case it simply returns an empty string.