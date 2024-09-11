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
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]  # get prefix before palindromic suffix
            return string + postfix + prefix[::-1]  # append reverse of prefix

    raise ValueError(f"No palindromic postfix found for string: {string}")


# Example usage
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome(''))  # ''
```

This Python script implements the `is_palindrome` function to check if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function iterates through the string from the end to find the longest palindromic postfix, and then appends the reverse of the prefix that comes before the palindromic suffix to create the shortest palindrome.