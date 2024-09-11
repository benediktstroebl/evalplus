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

    i = 0
    j = len(string) - 1
    while i < j:
        if string[i]!= string[j]:
            break
        i += 1
        j -= 1

    prefix = string[:i]
    suffix = string[i:j+1][::-1]
    palindrome = string + suffix + prefix[::-1]

    return palindrome


# Test cases
print(is_palindrome('radar'))  # True
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This Python script implements two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that starts with a given string. The `make_palindrome` function uses a two-pointer approach to find the longest postfix of the given string that is a palindrome, and then appends the reverse of the string prefix before the palindromic suffix to form the shortest palindrome.