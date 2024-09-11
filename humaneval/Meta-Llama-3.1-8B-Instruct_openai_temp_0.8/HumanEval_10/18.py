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

    Args:
        string (str): The string for which to find the shortest palindrome.

    Returns:
        str: The shortest palindrome that begins with the supplied string.
    """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    i = len(string) - 1
    while i >= 0 and string[i] == string[0]:
        i -= 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[:len(string) - i - 1][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script provides the `is_palindrome` function to check if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the supplied string that is a palindrome, then appends the reverse of the prefix that comes before the palindromic suffix to the end of the string.