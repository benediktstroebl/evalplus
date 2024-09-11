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

    return string + string[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome. It does this by checking all postfixes of the string, from longest to shortest, and returning the first one that is a palindrome. It then appends the reverse of the prefix that comes before this palindromic suffix to the end of the string. If no palindromic postfix is found, it simply appends the reverse of the entire string to the end of the string, effectively making the entire string a palindrome.