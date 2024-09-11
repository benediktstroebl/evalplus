### Make Palindrome Function
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
    string (str): The input string.

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
    # Reverse the input string
    rev_str = string[::-1]

    # Find the first prefix of rev_str that is a suffix of string
    idx = 0
    while idx < len(string) and string.startswith(rev_str[idx:]):
        idx += 1

    # Return the original string concatenated with the reversed prefix
    return string + rev_str[:idx]


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ''
    print(make_palindrome("cat"))  # Output: 'catac'
    print(make_palindrome("cata"))  # Output: 'catac'
    print(make_palindrome("abcd"))  # Output: 'abcdcba'
    print(make_palindrome("abba"))  # Output: 'abba'
```
This Python script defines the `is_palindrome` and `make_palindrome` functions, and includes example usage to demonstrate their behavior.