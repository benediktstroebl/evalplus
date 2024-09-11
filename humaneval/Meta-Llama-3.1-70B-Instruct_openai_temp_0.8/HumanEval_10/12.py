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

    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abccba'))  # 'abccba'
```
This Python script defines a function `make_palindrome` to find the shortest palindrome that begins with a supplied string. It uses the `is_palindrome` helper function to check whether a string is a palindrome. The `make_palindrome` function iterates over the postfixes of the input string from the longest to the shortest, and as soon as it finds a palindromic postfix, it appends the reverse of the corresponding prefix to the end of the string and returns the result. If no palindromic postfix is found, it simply appends the reverse of the input string to itself.