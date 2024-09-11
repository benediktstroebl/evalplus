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
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Test the functions
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

In the `make_palindrome` function, we start by checking the entire string to see if it's a palindrome. If it is, we simply return the string as it's already a palindrome. If not, we move on to the second longest postfix of the string and check if it's a palindrome. We continue this process until we find a postfix that's a palindrome.

Once we find a palindromic postfix, we append the reverse of the prefix that comes before it to the end of the string, effectively making the entire string a palindrome. This process ensures that we find the shortest palindrome possible that begins with the supplied string.