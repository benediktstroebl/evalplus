Here's the code to create the `make_palindrome` function, which receives a string and returns the shortest palindrome that begins with the provided string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.

    Algorithm idea simple simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    """ Returns tested longest palindrome for the given string:

    Example usage:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    >>> make_palindrome('abcde')
    'abcdeead'
    """
    if not string:
        return ""
    palindrome = string[::-1] + string[:len(string)//2]
    else:
        palindrome = string[::-1] + string[:len(string)//2] + string[len(string)//2:]
    return palindrome
```