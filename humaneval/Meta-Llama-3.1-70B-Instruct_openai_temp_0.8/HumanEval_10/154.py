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


# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```
This script defines two functions: `is_palindrome`, which checks if a string is a palindrome, and `make_palindrome`, which finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function does this by finding the longest postfix of the supplied string that is a palindrome and then appending the reverse of the prefix that comes before this palindromic suffix. If the input string is already a palindrome, it is returned unchanged.