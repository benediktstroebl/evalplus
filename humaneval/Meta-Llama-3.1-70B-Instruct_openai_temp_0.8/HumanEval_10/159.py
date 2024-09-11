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

    rev_string = string[::-1]
    for i in range(len(string), -1, -1):
        if is_palindrome(string + rev_string[i:]):
            return string + rev_string[i:]

# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script first defines a helper function `is_palindrome(string: str) -> bool` to test whether a given string is a palindrome. It then defines the main function `make_palindrome(string: str) -> str` to find the shortest palindrome that begins with a supplied string.

In the `make_palindrome(string: str) -> str` function, it first checks if the input string is empty, in which case it returns an empty string. Then, it iterates through the string in reverse order to find the longest postfix that is a palindrome. Once it finds such a postfix, it appends the reverse of the remaining prefix to the original string and returns the result.

The example use cases demonstrate how to use the `make_palindrome(string: str) -> str` function to find the shortest palindrome for different input strings.