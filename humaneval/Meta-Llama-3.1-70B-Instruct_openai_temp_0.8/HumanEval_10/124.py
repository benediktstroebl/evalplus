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
    if not string:  # edge case: empty string
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i - 1:]
        if is_palindrome(postfix):
            # Append the reverse of the prefix to the end of the string
            prefix = string[:i - 1]
            return string + prefix[::-1]

    # if no palindromic postfix found (which should be impossible), return the string itself
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('radar'))  # 'radar'
print(make_palindrome('hello'))  # 'helloolleh'
```