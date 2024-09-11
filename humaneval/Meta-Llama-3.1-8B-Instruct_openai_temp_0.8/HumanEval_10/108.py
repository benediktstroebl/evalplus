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
    if string == "":
        return ""
    
    # Find the longest postfix of supplied string that is a palindrome
    palindromic_suffix_len = 0
    for i in range(1, len(string) + 1):
        if is_palindrome(string[-i:]):
            palindromic_suffix_len = i
        else:
            break
    
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-palindromic_suffix_len]
    suffix = string[-palindromic_suffix_len:]
    palindrome = string + suffix[::-1]
    return palindrome


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `is_palindrome` to check if a string is a palindrome and a function `make_palindrome` to find the shortest palindrome that begins with a supplied string. It also includes test cases to verify the correctness of the `make_palindrome` function.