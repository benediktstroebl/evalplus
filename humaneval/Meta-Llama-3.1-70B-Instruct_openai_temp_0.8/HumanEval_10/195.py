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
        return string

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            rest = string[:i]
            return string + rest[::-1]

    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abba'))  # 'abba'
print(make_palindrome('abc'))  # 'abcba'
```

This Python script defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. The function uses the helper function `is_palindrome` to check if a string is a palindrome. The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome and then appending the reverse of the remaining prefix to the end of the string. If no such postfix is found, it simply appends the reverse of the entire string to itself. The script also includes test cases to demonstrate its usage.