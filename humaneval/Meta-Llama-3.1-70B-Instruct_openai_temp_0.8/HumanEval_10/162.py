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

    # find longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            break

    # append reverse of prefix to the end
    return string + string[:i-1][::-1]


# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```

The `make_palindrome` function works by first finding the longest palindromic suffix of the input string. It does this by checking all suffixes of the string from longest to shortest. Once it finds a palindromic suffix, it appends the reverse of the prefix that comes before the suffix to the end of the string. This results in the shortest palindrome that begins with the input string.