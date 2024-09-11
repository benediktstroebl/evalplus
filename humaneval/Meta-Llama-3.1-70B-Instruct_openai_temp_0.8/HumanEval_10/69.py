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
    if not string:  # if string is empty
        return ''

    # find the longest postfix that is a palindrome
    postfix_len = next((i for i in range(len(string), -1, -1) if is_palindrome(string[i:])), None)

    # reverse the prefix that comes before the palindromic postfix
    prefix_reversed = string[:postfix_len-1][::-1] if postfix_len > 0 else ''

    # append the reversed prefix to the end of the original string
    return string + prefix_reversed


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```