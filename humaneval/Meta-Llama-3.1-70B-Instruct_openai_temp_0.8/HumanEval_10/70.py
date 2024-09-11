```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome
    :param string: Input string to check
    :return: True if the string is a palindrome, False otherwise
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    :param string: Input string to make palindrome
    :return: The shortest palindrome that begins with the supplied string
    """
    # Handle edge case where string is empty
    if not string:
        return string

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i - 1:]):
            return string + string[:i - 1][::-1]

    # If no palindromic suffix is found, append the reverse of the string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```