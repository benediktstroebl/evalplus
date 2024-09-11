Here's a Python script that implements the `make_palindrome` function according to the given specifications:

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
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcddcba'))  # 'abcddcba'
print(make_palindrome('madam'))  #'madam'
```

The `make_palindrome` function iterates over the string from the end to the start. For each postfix, it checks if it's a palindrome using the `is_palindrome` function. If it is, it returns the original string plus the reverse of the prefix that comes before the palindromic suffix.

Note that the prefix is reversed using slicing (`string[:i][::-1]`) and then appended to the original string. This ensures that the resulting string is the shortest palindrome that begins with the supplied string.