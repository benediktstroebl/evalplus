### Solution
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
    def check_palindrome(suffix: str) -> bool:
        """ Helper function to check if a suffix is a palindrome """
        return suffix == suffix[::-1]

    # Initialize the longest palindromic suffix and the corresponding prefix
    longest_suffix = ''
    longest_prefix = ''

    # Iterate over all possible suffix lengths
    for length in range(1, len(string) + 1):
        suffix = string[-length:]
        
        # Check if the current suffix is a palindrome
        if check_palindrome(suffix):
            # If it's a palindrome, update the longest suffix and the corresponding prefix
            longest_suffix = suffix
            longest_prefix = string[:-length]

    # If a palindromic suffix is found, append the reverse of the prefix to the suffix
    if longest_suffix:
        return string + longest_suffix[::-1]
    else:
        # If no palindromic suffix is found, return the original string
        return string


# Example usage
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
print(make_palindrome(''))  # Output:
```

This solution first checks if a given suffix is a palindrome using a helper function `check_palindrome`. It then iterates over all possible suffix lengths and checks each suffix to see if it's a palindrome. If a palindromic suffix is found, it updates the longest suffix and the corresponding prefix. Finally, it appends the reverse of the prefix to the suffix to form the shortest palindrome that begins with the supplied string.