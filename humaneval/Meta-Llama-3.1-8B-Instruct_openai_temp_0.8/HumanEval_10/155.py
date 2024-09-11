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

    # Find the longest palindromic suffix of the string
    palindrome_suffix = ''
    for i in range(len(string) - 1, -1, -1):
        if string[i:] == string[i:][::-1]:
            palindrome_suffix = string[i:]
            break

    # Find the rest of the palindrome
    palindrome_prefix = string[:-len(palindrome_suffix)]
    palindrome_prefix = palindrome_prefix[::-1]

    return string + palindrome_prefix


# Test cases
print(is_palindrome('radar'))  # Expected: True
print(is_palindrome('python'))  # Expected: False
print(make_palindrome(''))  # Expected: ''
print(make_palindrome('cat'))  # Expected: 'catac'
print(make_palindrome('cata'))  # Expected: 'catac'
```