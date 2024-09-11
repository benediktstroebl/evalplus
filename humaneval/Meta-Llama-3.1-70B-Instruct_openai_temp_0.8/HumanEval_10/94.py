```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

    Args:
    string (str): The string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
    string (str): The string to be converted into a palindrome.

    Returns:
    str: The shortest palindrome that begins with the supplied string.
    """
    if not string:
        # If the string is empty, return it immediately
        return string

    # Find the longest postfix that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i-1:]
        if is_palindrome(postfix):
            # Append the reverse of the prefix to the string
            return string + string[:i-1][::-1]

    # If no postfix is found, append the reverse of the string to itself
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```