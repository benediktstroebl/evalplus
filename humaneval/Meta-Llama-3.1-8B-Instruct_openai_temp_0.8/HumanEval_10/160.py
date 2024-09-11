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

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Find the longest palindromic prefix
            for j in range(i):
                prefix = string[:-i+j]
                if is_palindrome(prefix):
                    # Append the reverse of the prefix
                    return string + prefix[::-1]
    
    # If no palindrome is found, return the original string
    return string


# Example usage:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script includes the two functions `is_palindrome` and `make_palindrome` as specified. It uses the `is_palindrome` function to check for palindromes and the `make_palindrome` function to find the shortest palindrome beginning with a supplied string.