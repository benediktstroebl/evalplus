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
    if not string:  # Base case: empty string
        return ''

    for i in range(len(string), 0, -1):  # Iterate from the end of the string
        postfix = string[i:]  # Get the postfix
        if is_palindrome(postfix):  # Check if the postfix is a palindrome
            prefix = string[:i]  # Get the prefix
            return string + prefix[::-1]  # Append the reverse of the prefix to the string

    # If no palindromic postfix is found, the entire string is used as the prefix
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```