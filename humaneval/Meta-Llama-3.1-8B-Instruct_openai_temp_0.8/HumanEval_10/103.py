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
    def is_POSTFIX_palindrome(s):
        """ Check if postfix of given string is a palindrome """
        return s == s[::-1]

    # Find the longest palindromic postfix
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_POSTFIX_palindrome(postfix):
            palindrome_suffix = postfix
            break

    # Form the shortest palindrome
    palindrome_prefix = string[:len(string) - len(palindrome_suffix)]
    return string + palindrome_prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script now includes the implementation of the `make_palindrome` function as per the provided specification. It first finds the longest palindromic postfix of the input string, and then appends the reverse of the prefix that comes before the palindromic suffix to form the shortest palindrome that begins with the supplied string.