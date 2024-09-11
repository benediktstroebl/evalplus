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

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            palindromic_suffix = string[i-1:]
            non_palindromic_prefix = string[:i-1]
            break
    else:
        # If no palindromic suffix is found, use the entire string as non_palindromic_prefix
        palindromic_suffix = ''
        non_palindromic_prefix = string

    # Append reverse of non_palindromic_prefix to the end of the string and its palindromic suffix
    return string + non_palindromic_prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```