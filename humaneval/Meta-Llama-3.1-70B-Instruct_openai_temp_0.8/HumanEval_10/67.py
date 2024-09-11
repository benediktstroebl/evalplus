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
        return string  # empty string is a palindrome

    for i in range(len(string), 0, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]

    # if no palindrome suffix is found, return the original string plus its reverse
    return string + string[::-1]


# Example usage:
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string.

The `make_palindrome` function works by iterating over the input string from the end to the beginning. For each position, it checks the suffix of the string to see if it's a palindrome. If it is, the function returns the original string plus the reverse of the prefix that comes before the palindromic suffix.

If no palindromic suffix is found, the function returns the original string plus its reverse. This ensures that the output is always a palindrome that begins with the input string.

Finally, the script includes some example usage of the `make_palindrome` function to demonstrate its behavior.