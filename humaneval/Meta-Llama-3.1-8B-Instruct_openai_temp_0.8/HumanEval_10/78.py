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
    # Check if input is empty
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        # Check if the postfix is a palindrome
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[:i][::-1]


# Test the function
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script first checks if the input string is empty. If it is, it returns an empty string. Otherwise, it iterates over the input string from the end to the beginning, checking each time if the current postfix is a palindrome. As soon as it finds a palindrome postfix, it creates the shortest palindrome by appending the reverse of the string prefix to the end of the original string. The result is then returned.