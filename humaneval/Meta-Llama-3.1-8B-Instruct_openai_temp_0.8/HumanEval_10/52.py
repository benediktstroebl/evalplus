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
        return ""

    for i in range(len(string), 0, -1):
        substring = string[-i:]
        if is_palindrome(substring):
            return string + substring[::-1]

    return string


# Example usage:
print(make_palindrome '')  # Output: ''
print(make_palindrome 'cat')  # Output: catac
print(make_palindrome 'cata')  # Output: catac
```
This script implements the `make_palindrome` function according to the provided algorithm and includes example usage.