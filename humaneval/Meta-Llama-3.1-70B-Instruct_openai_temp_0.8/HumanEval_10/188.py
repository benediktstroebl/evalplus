Here's a self-contained Python script implementing the `make_palindrome` function as described in the problem:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
    string (str): Input string.

    Returns:
    str: Shortest palindrome beginning with the supplied string.

    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:  # Base case: empty string
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Append reverse of the string prefix before the palindromic suffix
            prefix = string[:-i] if i < len(string) else ''
            return string + prefix[::-1]

    # If no palindromic postfix is found, append the reversed string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script implements the `make_palindrome` function by finding the longest postfix of the input string that is a palindrome and appending the reverse of the string prefix before this palindromic suffix. The script includes test cases to verify the correctness of the function.