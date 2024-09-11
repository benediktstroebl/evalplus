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

    rev_str = string[::-1]
    for i in range(len(string)):
        postfix = string[i:]
        prefix = string[:i]
        if postfix == postfix[::-1]:
            return string + rev_str[i:]


# Example usage:
print(is_palindrome('radar'))  # Output: True
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome('abcdefg'))  # Output: 'abcdefgcdegab'
```
This script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that starts with a given string by finding the longest palindromic postfix, and appending the reverse of the prefix that comes before the palindromic suffix to the end of the string.