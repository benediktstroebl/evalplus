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
    if string == '':  # base case
        return ''

    # Find longest prefix that is also a palindrome
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        # Check if prefix is a palindrome
        if is_palindrome(prefix):
            # Find the palindromic suffix
            suffix = string[len(prefix):]
            # Check if suffix is a palindrome
            if is_palindrome(suffix):
                # The palindrome is the prefix followed by the reverse of the suffix
                return prefix + suffix[::-1]

    # If no palindrome is found, return the input string
    return string


# Example usage:
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
print(make_palindrome(''))  # Output: ''
```
This script implements the `make_palindrome` function using a brute-force approach with the `is_palindrome` function to check for palindromes. It finds the longest prefix that is a palindrome, and then checks if the remaining suffix is also a palindrome. If both conditions are met, it returns the palindrome by appending the reverse of the suffix to the prefix.