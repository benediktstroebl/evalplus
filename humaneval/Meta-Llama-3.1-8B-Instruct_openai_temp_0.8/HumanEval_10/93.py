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
    if not string:  # edge case for empty string
        return ''

    # Find the longest palindromic suffix of the input string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            # Reverse the prefix that comes before the palindromic suffix
            palindrome = string + string[:len(string) - i][::-1]
            return palindrome

# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In this script, we define the `make_palindrome` function which works as described in the docstring. It iterates from the end of the input string to find the longest palindromic suffix, and then appends the reverse of the prefix that comes before the palindromic suffix. The `is_palindrome` function is used to check if a given string is a palindrome.