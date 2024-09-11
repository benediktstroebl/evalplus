```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
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

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    # This should not be reached, but if it is, it means no palindrome was found.
    return string


# Test the function with provided examples
print(make_palindrome(''))  # Should print: ''
print(make_palindrome('cat'))  # Should print: 'catac'
print(make_palindrome('cata'))  # Should print: 'catac'
```
This script defines two functions: `is_palindrome` checks whether a given string is the same forwards and backwards, and `make_palindrome` uses this function to find the shortest palindrome that begins with a given string. The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome, then appending the reverse of the prefix that comes before this postfix.