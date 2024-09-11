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
        # Check if the postfix of length i is a palindrome
        if is_palindrome(string[-i:]):
            # Append the reverse of the prefix to the string
            return string + string[:-i][::-1]
    # If the string itself is a palindrome, return it
    return string


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

This Python script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` generates the shortest palindrome starting with the input string. The `make_palindrome` function iterates from the longest to the shortest postfix of the input string, checking if each postfix is a palindrome. When a palindromic postfix is found, the function appends the reverse of the corresponding prefix to the input string to form the shortest palindrome. The script includes test cases to demonstrate its functionality.