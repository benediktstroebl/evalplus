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

    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    # if no palindromic postfix found, append reversed string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This script uses a simple iterative approach to find the longest palindromic postfix of the input string, then appends the reverse of the remaining prefix to form the shortest palindrome. If no palindromic postfix is found, it simply appends the reverse of the entire string.