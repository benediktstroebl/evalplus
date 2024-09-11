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

    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and string[i] == string[-1-i]:
        i += 1
    if i < len(string) // 2:
        # If not entire string forms a palindrome, then the longest palindromic postfix is a proper substring of it
        palindrome_suffix = string[:i]
    else:
        palindrome_suffix = string

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindrome_suffix[::-1] if string!= palindrome_suffix else string


# Test cases
print(is_palindrome('radar'))  # True
print(is_palindrome('python'))  # False
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('level'))  # 'level'
```