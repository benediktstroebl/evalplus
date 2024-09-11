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
    # If the string is empty or already a palindrome, return the string as it is
    if is_palindrome(string):
        return string

    # Find the longest palindromic postfix
    longest_postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            longest_postfix = string[i-1:]
            break

    # Append the reverse of the prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(longest_postfix)]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```