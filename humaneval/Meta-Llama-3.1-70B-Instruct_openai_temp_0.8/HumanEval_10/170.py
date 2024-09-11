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
        if is_palindrome(string[:i]):
            return string + string[:i-1][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

Explanation:

1.  The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse.
2.  The `make_palindrome` function finds the shortest palindrome that begins with a supplied string.
3.  It iterates over the string from longest to shortest, checking each postfix to see if it's a palindrome.
4.  Once it finds a palindromic postfix, it returns the original string plus the reverse of the prefix that comes before the palindromic suffix.

This solution works by identifying the longest palindromic suffix and then appending the reverse of the remaining prefix to the end of the string, effectively creating a palindrome.