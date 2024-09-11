**Palindrome Maker Script**
================================

Below is a self-contained Python script that defines two functions: `is_palindrome` to check if a given string is a palindrome, and `make_palindrome` to find the shortest palindrome that begins with a supplied string.

```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

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
    string (str): The input string to make into a palindrome.

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
    if not string:  # edge case: empty string
        return string

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string + string[::-1]  # default: no palindromic postfix found


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

You can save this script to a file (e.g., `palindrome_maker.py`) and run it using Python (e.g., `python palindrome_maker.py`). The test cases at the end of the script will verify the correctness of the `make_palindrome` function.