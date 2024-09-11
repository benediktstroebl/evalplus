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
    if not string:  # Empty string is a palindrome
        return ''

    # Find the longest postfix that is a palindrome
    i = 0
    while i < len(string) and is_palindrome(string[i:]):
        i += 1

    # Find the longest prefix that is a palindrome
    j = 0
    while j < len(string) and is_palindrome(string[:j+1]):
        j += 1

    # If the string is already a palindrome, return it
    if i == j:
        return string

    # Return the palindrome that starts with the input string
    return string + string[j-i+1:i:-1]


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In this code, we first check if the string is empty, in which case it is a palindrome. Then we find the longest postfix that is a palindrome, and the longest prefix that is a palindrome. If the string is already a palindrome, we return it. Otherwise, we return the shortest palindrome that starts with the input string by appending the reverse of the prefix to the end of the string.