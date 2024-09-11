```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:  # Empty string is a palindrome
        return ''

    # Find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            break

    # The non-palindromic prefix
    prefix = string[:i-1]

    # Append the reverse of the prefix to the original string
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('abc'))  # Expected output: 'abcba'
print(make_palindrome('abba'))  # Expected output: 'abba'
```