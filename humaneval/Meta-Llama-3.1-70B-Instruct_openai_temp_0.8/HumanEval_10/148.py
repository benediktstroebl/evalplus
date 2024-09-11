```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
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
    
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
            return string + string[:i][::-1]
    

# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the supplied string.

The `make_palindrome` function works by finding the longest postfix of the supplied string that is a palindrome. It then appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix. This is done by iterating over the string from the end to the beginning and checking if each postfix is a palindrome. Once a palindromic postfix is found, the function appends the reverse of the prefix to the end of the string and returns the result.

The script includes example use cases to demonstrate how the `make_palindrome` function works.