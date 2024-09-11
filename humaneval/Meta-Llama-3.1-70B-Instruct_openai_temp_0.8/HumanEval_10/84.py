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
    if not string:  # if string is empty
        return ''

    for i in range(len(string), 0, -1):  # iterate from the end of the string
        postfix = string[i:]  # get the postfix
        if is_palindrome(postfix):  # if postfix is a palindrome
            prefix = string[:i]  # get the prefix
            return string + prefix[::-1]  # return the palindrome

    # if no palindromic postfix is found, the whole string is already a palindrome
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```