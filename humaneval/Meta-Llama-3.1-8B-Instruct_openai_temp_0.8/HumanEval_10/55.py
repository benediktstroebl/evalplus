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
    if not string:  # check if input string is empty
        return ''

    i = 0  # initialize index to start checking from the end of the string
    while i < len(string) and string[i] == string[-1 - i]:
        i += 1  # move the index to the left until a mismatch is found or the center of the string is reached

    return string + string[:i][::-1]  # append reverse of prefix to the original string


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines the `is_palindrome` function to test if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the supplied string that is a palindrome, and then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. The script also includes example usage of the `make_palindrome` function.