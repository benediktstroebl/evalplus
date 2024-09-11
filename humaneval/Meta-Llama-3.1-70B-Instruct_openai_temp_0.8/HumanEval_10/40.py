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

    Examples:
        >>> make_palindrome('')
        ''
        >>> make_palindrome('cat')
        'catac'
        >>> make_palindrome('cata')
        'catac'
    """
    # Handle empty string
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    postfix_length = 0
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            postfix_length = i
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-postfix_length]
    return string + prefix[::-1]


# Test the function
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```