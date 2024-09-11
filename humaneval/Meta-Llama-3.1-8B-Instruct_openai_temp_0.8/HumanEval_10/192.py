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
    def is_palindrome_suffix(s: str) -> int:
        """ Find the length of the longest palindromic suffix of a string """
        n = len(s)
        i = 0
        while i < n and s[i] == s[n - i - 1]:
            i += 1
        return i

    return string + string[:is_palindrome_suffix(string)][::-1]


print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
```

This script defines two functions, `is_palindrome` and `make_palindrome`, as specified. The `make_palindrome` function uses a helper function `is_palindrome_suffix` to find the length of the longest palindromic suffix of the input string. It then returns the input string with the reverse of the string prefix (before the palindromic suffix) appended to the end.