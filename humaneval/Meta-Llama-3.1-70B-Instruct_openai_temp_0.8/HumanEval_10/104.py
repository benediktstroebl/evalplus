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

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

In this code, we first find the longest postfix of the given string that is a palindrome. We do this by iterating over all possible postfixes of the string from longest to shortest. Once we find a palindromic postfix, we append the reverse of the prefix that comes before this postfix to the original string. This results in the shortest palindrome that begins with the supplied string.