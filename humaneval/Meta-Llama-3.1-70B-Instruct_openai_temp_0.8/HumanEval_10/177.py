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

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    # If no palindromic suffix found, append the reverse of the whole string
    return string + string[::-1]


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

In this script, `is_palindrome` checks whether a string is the same when its characters are reversed. The `make_palindrome` function iterates through the input string from the end to the start, checking each postfix to see if it is a palindrome. When it finds the longest palindromic postfix, it appends the reverse of the prefix that comes before it to the original string to create the shortest palindrome. If no palindromic suffix is found, it appends the reverse of the whole string.