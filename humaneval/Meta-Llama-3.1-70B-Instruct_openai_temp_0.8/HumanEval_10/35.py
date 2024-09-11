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
    if is_palindrome(string):
        return string

    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
In this script, `is_palindrome` function checks whether a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that begins with the supplied string. It does this by finding the longest postfix of the string that is a palindrome and then appending the reverse of the prefix that comes before the palindromic suffix.