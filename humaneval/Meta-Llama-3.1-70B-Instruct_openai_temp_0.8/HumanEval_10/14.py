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
    string (str): Input string to be converted into a palindrome.

    Returns:
    str: The shortest palindrome that begins with the supplied string.

    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string or is_palindrome(string):
        return string
    
    rev_string = string[::-1]
    
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:] + rev_string):
            return string + rev_string[:i]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks whether a string is a palindrome, and `make_palindrome` generates the shortest palindrome that starts with the input string. The `make_palindrome` function works by first checking if the input string is already a palindrome or empty. If not, it finds the longest palindromic postfix of the input string by checking all possible postfixes in reverse order. Once found, it appends the reverse of the prefix that comes before the palindromic postfix to the input string.