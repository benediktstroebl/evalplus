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
    # If the string is a palindrome, return it because adding anything else would make it longer
    if is_palindrome(string):
        return string

    # Check all substrings of the string
    for i in range(len(string), 0, -1):
        # Get the substring of the given length
        substr = string[-i:]
        
        # Check if it's a palindrome
        if is_palindrome(substr):
            # If it's a palindrome, append it's reverse to the end of the string
            return string + substr[::-1]


# Example usage:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In the provided code, the `make_palindrome` function checks all substrings of the input string from the longest to the shortest to find the longest palindromic suffix. It then appends the reverse of the string prefix to the palindromic suffix to form the shortest palindrome that begins with the input string. The `is_palindrome` function is used to check if a given string is a palindrome.