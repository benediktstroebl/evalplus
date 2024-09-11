```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome

    Args:
    string (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
    string (str): The input string to convert to a palindrome.

    Returns:
    str: The shortest palindrome that begins with the input string.
    """
    if is_palindrome(string):
        # If the input string is already a palindrome, return it as is.
        return string

    # Find the longest postfix of the input string that is a palindrome.
    postfix_len = 0
    while postfix_len < len(string) and not is_palindrome(string[postfix_len:]):
        postfix_len += 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    prefix = string[:postfix_len]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```