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
    if not string:  # Return empty string for empty input
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(1, len(string) + 1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            palindrome_suffix = postfix
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-len(palindrome_suffix)]
    palindrome = string + prefix[::-1]
    return palindrome


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines a function `make_palindrome` that finds the shortest palindrome that begins with a supplied string. The function uses a helper function `is_palindrome` to test if a given string is a palindrome. The main function iterates over the postfixes of the string to find the longest one that is a palindrome. It then appends the reverse of the string prefix that comes before the palindromic suffix to form the shortest palindrome.