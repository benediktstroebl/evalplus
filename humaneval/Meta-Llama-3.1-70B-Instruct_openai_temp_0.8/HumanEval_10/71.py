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
        # Find the longest palindromic postfix
        if is_palindrome(string[i:]):
            # Append reverse of prefix to the palindromic postfix
            return string + string[:i][::-1]
    # If no palindromic postfix found, return the string twice reversed
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected: ''
print(make_palindrome('cat'))  # Expected: 'catac'
print(make_palindrome('cata'))  # Expected: 'catac'
```

This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the string that is a palindrome, and then appending the reverse of the prefix that comes before this palindromic suffix. The test cases are also included to verify the correctness of the functions.