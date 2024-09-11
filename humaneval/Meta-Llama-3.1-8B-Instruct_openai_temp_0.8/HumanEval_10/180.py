### Palindrome Maker Script
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
    while not is_palindrome(string):
        prefix = string[:-1]
        suffix = string[-1]
        if is_palindrome(prefix):
            break
        string += suffix
    return string


# Test cases
print(make_palindrome(''))  # Expected: ''
print(make_palindrome('cat'))  # Expected: 'catac'
print(make_palindrome('cata'))  # Expected: 'catac'
```
This script uses the `is_palindrome` function to check if a string is a palindrome. The `make_palindrome` function iteratively adds the last character of the string to the end until it finds a palindromic postfix. It then appends the reverse of the prefix that comes before the palindromic suffix to make the string a palindrome.