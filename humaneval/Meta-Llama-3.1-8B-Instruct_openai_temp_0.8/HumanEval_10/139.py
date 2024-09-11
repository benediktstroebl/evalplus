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
    def is_palindrome_suffix(suffix: str) -> bool:
        """ Check if suffix is a palindrome """
        return suffix == suffix[::-1]

    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Initialize longest non-palindrome prefix
    longest_prefix = ''
    # Iterate over the string from the end to the start
    for i in range(len(string) - 1, -1, -1):
        prefix = string[:i+1]
        # Check if the rest of the string is a palindrome
        suffix = string[i+1:]
        if is_palindrome_suffix(suffix):
            # If it is, update the longest non-palindrome prefix
            longest_prefix = prefix
            break

    # If the string is not a palindrome, construct the shortest palindrome
    # by appending the reverse of the longest non-palindrome prefix
    palindrome = string + string[:len(longest_prefix)-1][::-1]

    return palindrome


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
```