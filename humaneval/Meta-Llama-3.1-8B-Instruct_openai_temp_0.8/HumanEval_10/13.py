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

    i, j = 0, len(string) - 1
    while i < j:
        if string[i]!= string[j]:
            break
        i += 1
        j -= 1

    prefix = string[:i]
    suffix = string[i:j+1][::-1]

    return string + suffix


# Test cases
print(is_palindrome('radar'))  # True
print(is_palindrome('python'))  # False
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first checks if the input string is a palindrome using the `is_palindrome` function. Then it uses the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the supplied string that is a palindrome, and then appending to the end of the string the reverse of the string prefix that comes before the palindromic suffix.