```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome

    Args:
    string (str): The string to check.

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
    string (str): The string to convert to a palindrome.

    Returns:
    str: The shortest palindrome that begins with the supplied string.
    """
    # If the string is already a palindrome, return it as is
    if is_palindrome(string):
        return string

    # Iterate over the string in reverse to find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[i-1:]
        if is_palindrome(postfix):
            # Find the prefix that comes before the palindromic postfix
            prefix = string[:i-1]
            # Return the string with the reverse of the prefix appended to the end
            return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```