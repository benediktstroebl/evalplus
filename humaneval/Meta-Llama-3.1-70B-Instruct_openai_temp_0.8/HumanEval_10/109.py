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

    # Initialize longest palindromic postfix
    longest_postfix = ''

    # Iterate over length of string
    for i in range(len(string), 0, -1):
        # Check if i-th postfix is a palindrome
        postfix = string[-i:]
        if is_palindrome(postfix):
            longest_postfix = postfix
            break

    # Find prefix before longest palindromic postfix
    prefix = string[:-len(longest_postfix)]

    # Append reverse of prefix to end of string
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('abc'))  # Expected output: 'abcba'
```