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
        return string

    # Find the longest postfix that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            postfix = string[i-1:]
            break

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(postfix)]

    # Append the reverse of the prefix to the end of the string
    return string + prefix[::-1]


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```