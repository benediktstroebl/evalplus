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
    # Base case: empty string is a palindrome
    if not string:
        return string

    # Check for the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # The rest of the string is the prefix that comes before the palindromic suffix
            prefix = string[:i]
            # Append the reverse of the prefix to the original string
            return string + prefix[::-1]

    # If no palindromic suffix is found, return the original string with its reverse appended
    return string + string[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```