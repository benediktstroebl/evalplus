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

    # Iterate over the input string from the end to the start
    for i in range(len(string), 0, -1):
        # Check if the current postfix is a palindrome
        if is_palindrome(string[-i:]):
            # If it's a palindrome, append the reverse of the prefix to the end of the string
            return string + string[:-i][::-1]

    # If no postfix is a palindrome, append the reverse of the entire string to the end
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```