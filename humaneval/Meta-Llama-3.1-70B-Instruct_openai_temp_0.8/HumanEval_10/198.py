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

    # Find the longest postfix that is a palindrome
    postfix_len = 0
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            postfix_len = i
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-postfix_len]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This script defines a function `is_palindrome` to check if a given string is a palindrome, and another function `make_palindrome` to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses the `is_palindrome` function to find the longest postfix of the string that is a palindrome, and then appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix.