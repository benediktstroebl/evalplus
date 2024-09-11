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

    # Find the longest palindrome suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Reverse the prefix and append it to the palindrome suffix
            return string[:i] + string[i:][::-1]


# Test the function
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
```

In this script, the `make_palindrome` function checks for the longest postfix of the input string that is a palindrome, and then appends the reverse of the string prefix to the palindrome suffix to create the shortest palindrome that begins with the supplied string. The `is_palindrome` function is used to check if a string is a palindrome.