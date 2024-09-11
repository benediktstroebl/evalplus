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
    # Handle the case when input string is empty
    if not string:
        return ''

    # Iterate through the string from end to start and find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[i-1:]
        if is_palindrome(postfix):
            # Append reverse of prefix that comes before the palindromic postfix
            return string + string[:i-1][::-1]

    # If no palindromic postfix is found, return the string appended with its reverse
    return string + string[::-1]


# Test cases
print(make_palindrome(""))  # Expected output: ''
print(make_palindrome("cat"))  # Expected output: 'catac'
print(make_palindrome("cata"))  # Expected output: 'catac'
```

The provided `make_palindrome` function implements the described algorithm. It works by finding the longest postfix of the input string that is a palindrome and then appending the reverse of the remaining prefix to the end of the string. If no palindromic postfix is found, it simply appends the reverse of the input string to itself.