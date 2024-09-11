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
    # Handle edge cases
    if not string:
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Append the reverse of the prefix to the end of the string
            prefix = string[:-i]
            return string + prefix[::-1]

    # If no postfix is found, return the string and its reverse
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome and then appending the reverse of the prefix to the end of the string. The script includes several test cases to demonstrate the functionality of the `make_palindrome` function.