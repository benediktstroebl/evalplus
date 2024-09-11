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
    rev_str = string[::-1]
    for i in range(len(string), -1, -1):
        if is_palindrome(string + rev_str[i:]):
            return string + rev_str[i:]
    return string + rev_str


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abccba'))  # 'abccba'
```

This script defines two functions, `is_palindrome` and `make_palindrome`, to solve the given problem. The `is_palindrome` function checks if a given string is a palindrome, and the `make_palindrome` function finds the shortest palindrome that begins with the supplied string. The `make_palindrome` function iterates from the end of the input string, checking if appending the reverse of the remaining string results in a palindrome. If so, it returns the result; otherwise, it continues to the next iteration.