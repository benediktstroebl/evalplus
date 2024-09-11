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
        # Check if postfix of the supplied string is a palindrome
        if is_palindrome(string[i:]):
            # Find the prefix that comes before the palindromic suffix
            prefix = string[:i]
            # Append the reverse of the prefix to the supplied string
            return string + prefix[::-1]
    # If the supplied string is empty or does not have any palindromic postfix, return the reverse of the string
    return string[::-1] + string


# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```