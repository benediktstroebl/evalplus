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
    # Handle edge case where string is empty
    if not string:
        return ''

    # Start from the end of the string
    for i in range(len(string), 0, -1):
        postfix = string[i - 1:]
        # Check if postfix is a palindrome
        if is_palindrome(postfix):
            # Get the prefix that comes before the palindromic suffix
            prefix = string[:i - 1]
            # Append the reverse of the prefix to the end of the string
            return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

This script works by iterating through the string from the end to the beginning, checking each postfix to see if it's a palindrome. When it finds the longest palindromic postfix, it appends the reverse of the prefix that comes before it to the end of the string, effectively creating the shortest palindrome that begins with the supplied string.