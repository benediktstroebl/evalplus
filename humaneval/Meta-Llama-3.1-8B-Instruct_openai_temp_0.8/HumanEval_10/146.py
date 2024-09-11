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
        return ""

    # Find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # If the longest palindromic suffix is the entire string, return it as is
            if i == len(string):
                return string
            # If the longest palindromic suffix is a proper substring, append the reverse of the prefix to it
            else:
                return string[:i] + string[i:][::-1]

# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```

This script defines the `is_palindrome` function to test if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function does this by finding the longest palindromic suffix of the string and appending the reverse of the prefix to it. The script then includes test cases to verify its correctness.