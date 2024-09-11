**Palindrome Maker Script**
==========================

Below is a Python script that defines two functions: `is_palindrome` to test if a given string is a palindrome, and `make_palindrome` to find the shortest palindrome that begins with a supplied string.

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if postfix == postfix[::-1]:
            prefix = string[:i]
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            palindrome = postfix + prefix[::-1]
            return palindrome

    return string


# Test cases
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("cat"))  # Expected output: False
print(is_palindrome("catac"))  # Expected output: True

print(make_palindrome(""))  # Expected output: ''
print(make_palindrome("cat"))  # Expected output: 'catac'
print(make_palindrome("cata"))  # Expected output: 'catac'
```

This script uses a brute-force approach to find the longest postfix of the input string that is a palindrome, then appends the reverse of the string prefix that comes before the palindromic suffix to form the shortest palindrome that begins with the supplied string. The `is_palindrome` function is used to test if a given string is a palindrome.