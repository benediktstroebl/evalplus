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
        str: Shortest palindrome that begins with the input string.
    
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

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-i]
    return string + prefix[::-1]


# Test cases
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ''
    print(make_palindrome("cat"))  # Output: 'catac'
    print(make_palindrome("cata"))  # Output: 'catac'
```