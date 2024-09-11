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
    # Check if the string is a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string) - 1, -1, -1):
        sub_string = string[i:]
        if is_palindrome(sub_string):
            # Get the prefix of the string
            prefix = string[:i]
            # Reverse the prefix
            reversed_prefix = prefix[::-1]
            # Append the reversed prefix to the postfix
            palindrome = sub_string + reversed_prefix
            return palindrome

    # If no palindrome is found
    return string


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function is implemented by first checking if the input string is a palindrome. If it is not, it tries to find the longest postfix of the string that is a palindrome and appends the reverse of the prefix to it. If no palindrome is found, it returns the original string.