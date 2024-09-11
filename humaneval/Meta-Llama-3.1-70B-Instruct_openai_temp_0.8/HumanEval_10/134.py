```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

    Args:
    string (str): Input string to be checked.

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
    string (str): Input string to be made into a palindrome.

    Returns:
    str: The shortest palindrome that begins with the input string.

    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:  # If the string is empty, return it immediately
        return string

    for i in range(len(string), 0, -1):  # Iterate from the end of the string
        postfix = string[i - 1:]  # Get the postfix of the current length
        if is_palindrome(postfix):  # Check if the postfix is a palindrome
            prefix = string[:i - 1]  # Get the prefix that comes before the palindrome
            return string + prefix[::-1]  # Return the palindrome by appending the reverse of the prefix

    # If no palindrome postfix is found, append the reverse of the entire string
    return string + string[::-1]


# Test the functions
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```