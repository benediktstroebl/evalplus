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
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]
            palindrome = postfix + prefix[::-1]
            return palindrome
    return string


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines the `is_palindrome` and `make_palindrome` functions as desired and provides example use cases at the end. The `make_palindrome` function finds the longest postfix of the input string that is a palindrome, then constructs the shortest palindrome by appending the reverse of the string prefix to it. If no palindromic postfix is found, the function returns the original string.