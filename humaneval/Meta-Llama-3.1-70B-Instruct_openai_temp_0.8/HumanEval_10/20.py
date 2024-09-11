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
        string (str): Input string.

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
    if not string:
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i - 1:]
        if is_palindrome(postfix):
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(postfix)]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```