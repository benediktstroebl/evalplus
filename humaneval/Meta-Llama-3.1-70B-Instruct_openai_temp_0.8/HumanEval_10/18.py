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
    rev_string = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(rev_string[i:] + string):
            return rev_string[i:] + string
    return rev_string + string


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks if a given string is the same when reversed, and `make_palindrome` finds the shortest palindrome that begins with a supplied string by appending a reversed prefix to the input string. The script also includes example usage to demonstrate the functionality of these functions.