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
    reverse = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(string + reverse[i:]):
            return string + reverse[i:]


# Test the functions
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('race'))  # Expected output: 'racecar'
print(make_palindrome('radar'))  # Expected output: 'radar'
```

In this code, the `make_palindrome` function generates the reverse of the input string and then checks for the longest postfix of the original string that is a palindrome by appending the reverse string to the original string from the end. It does this by iterating over the reverse string from the end to the beginning and checking if the resulting string is a palindrome. If it finds a palindrome, it returns that string.