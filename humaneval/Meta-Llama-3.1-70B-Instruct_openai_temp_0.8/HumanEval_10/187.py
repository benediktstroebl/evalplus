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
    # Handle edge case where input string is empty
    if not string:
        return ''

    # Iterate over the input string in reverse order to find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        # Check if the current suffix is a palindrome
        if is_palindrome(string[-i:]):
            # Calculate the non-palindromic prefix
            prefix = string[:-i]
            # Return the original string with the reversed prefix appended
            return string + prefix[::-1]

    # If no palindromic suffix is found, append the reversed input string
    return string + string[::-1]


# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```