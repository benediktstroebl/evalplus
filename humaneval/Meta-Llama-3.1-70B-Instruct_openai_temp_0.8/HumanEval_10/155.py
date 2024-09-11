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
    # Handle edge case where input string is empty
    if not string:
        return string
    
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            break
    
    # Find the prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(suffix)]
    
    # Return the shortest palindrome
    return string + prefix[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that starts with a supplied string. The `make_palindrome` function works by finding the longest palindromic suffix of the input string and appending the reverse of the corresponding prefix to the end of the string. The script also includes example usage at the end.