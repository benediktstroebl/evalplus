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
    # Edge case: empty string
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        # Check if the postfix is a palindrome
        if is_palindrome(string[i-1:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[:i-1][::-1]

    # Default case: if no palindromic suffix is found, just append the reverse of the string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcd'))  # 'abcdcba'
print(make_palindrome('abba'))  # 'abba'
```