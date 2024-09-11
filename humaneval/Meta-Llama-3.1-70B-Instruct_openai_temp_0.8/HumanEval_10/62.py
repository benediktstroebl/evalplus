```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Handle edge case
    if not string:
        return string

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Calculate the prefix that comes before the palindromic suffix
            prefix = string[:-i]
            # Append the reverse of the prefix to the string
            return string + prefix[::-1]

    # If no palindromic postfix is found, append the reverse of the entire string
    return string + string[::-1]


if __name__ == "__main__":
    test_cases = [
        ('', ''),
        ('cat', 'catac'),
        ('cata', 'catac')
    ]

    for string, expected in test_cases:
        result = make_palindrome(string)
        assert result == expected, f"make_palindrome('{string}') failed: expected '{expected}', got '{result}'"
        print(f"make_palindrome('{string}') passed: {result}")
```