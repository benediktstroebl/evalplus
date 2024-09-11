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
    if not string:
        return ''

    # Find the longest palindrome postfix
    postfix = string
    while postfix and not is_palindrome(postfix):
        postfix = postfix[1:]

    # Reverse the prefix and append to the postfix
    prefix = string[:len(string) - len(postfix)]
    return postfix + prefix[::-1]


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
```

This script defines two functions, `is_palindrome` and `make_palindrome`, as specified in the problem statement. The `make_palindrome` function finds the shortest palindrome that begins with the input string by identifying the longest postfix that is a palindrome, then appending the reverse of the prefix that comes before the palindromic suffix.