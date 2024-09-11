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
    # Handle edge case where string is empty
    if not string:
        return ''

    # Reverse the string to check for postfix palindrome
    reversed_string = string[::-1]

    # Find the longest postfix palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(reversed_string[:i]):
            postfix_palindrome = reversed_string[:i]
            break

    # If the string is already a palindrome, return it
    if postfix_palindrome == string:
        return string

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:-len(postfix_palindrome)]

    # Append the reverse of the prefix to the end of the string
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Should return ''
print(make_palindrome('cat'))  # Should return 'catac'
print(make_palindrome('cata'))  # Should return 'catac'
```

This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix palindrome of the input string, and then appends the reverse of the prefix that comes before the palindromic suffix to the end of the string.