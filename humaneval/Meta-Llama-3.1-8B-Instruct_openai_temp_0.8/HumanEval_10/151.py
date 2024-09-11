### Solution to Find the Shortest Palindrome

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
    if not string:  # edge case: empty string
        return ''

    # Find the longest palindromic suffix of the string
    for i in range(len(string), -1, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            break

    # Reverse the string prefix that comes before the palindromic suffix
    prefix = string[:i]
    palindrome = suffix + prefix[::-1]

    return palindrome


# Test the function
print(make_palindrome(""))  # ''
print(make_palindrome("cat"))  # catac
print(make_palindrome("cata"))  # catac
```

This script uses a brute force approach to find the longest palindromic suffix of the input string. It then reverses the prefix of the string that comes before the palindromic suffix and appends it to the palindromic suffix to form the shortest palindrome that begins with the input string.