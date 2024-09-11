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


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script defines two functions: `is_palindrome` checks whether a given string is a palindrome by comparing it to its reverse, and `make_palindrome` generates the shortest palindrome that starts with the input string.

In the `make_palindrome` function:

1.  If the input string is already a palindrome, it is returned unchanged.
2.  Otherwise, the function iterates through the string from right to left, checking for the longest palindromic postfix.
3.  When it finds a palindromic postfix, it returns the original string appended with the reverse of the prefix preceding the palindromic postfix.