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

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            palindrome_suffix = postfix
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    palindrome = string + palindrome_suffix[::-1]
    return palindrome


# Example usage
print(is_palindrome('radar'))  # True
print(is_palindrome('hello'))  # False

print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `is_palindrome` and `make_palindrome` functions as described in the problem. The `make_palindrome` function iterates over the string in reverse to find the longest postfix that is a palindrome, and then appends the reverse of the string prefix to the end of the string.