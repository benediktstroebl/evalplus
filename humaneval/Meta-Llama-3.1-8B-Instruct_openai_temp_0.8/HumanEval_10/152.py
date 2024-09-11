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
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[i:][::-1]
    
    # If no palindrome postfix found, return the original string
    return string


# Test cases
if __name__ == "__main__":
    print(make_palindrome(""))  # Expected output: ''
    print(make_palindrome("cat"))  # Expected output: 'catac'
    print(make_palindrome("cata"))  # Expected output: 'catac'
```

This script defines the `is_palindrome` and `make_palindrome` functions, and includes test cases to verify their correctness. The `make_palindrome` function iterates through the string from the end to find the longest postfix that is a palindrome, and then appends the reverse of the prefix to it to make the string a palindrome. If no palindrome postfix is found, it returns the original string.