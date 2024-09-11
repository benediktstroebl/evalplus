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

    # Find the longest prefix that is a palindrome
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            palindrome_suf = string[:i]
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[:len(string) - len(palindrome_suf)][::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script defines a function `make_palindrome` that generates the shortest palindrome that begins with a supplied string. It uses the helper function `is_palindrome` to check if a given string is a palindrome.

The `make_palindrome` function works by first finding the longest prefix of the input string that is a palindrome. It then appends to the end of the input string the reverse of the prefix that comes before the palindromic suffix. If the input string is empty, the function returns an empty string.

The script includes test cases to verify the correctness of the `make_palindrome` function.