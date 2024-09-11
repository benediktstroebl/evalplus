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
    # Handle edge case where input string is empty
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + prefix[::-1]

    # If no palindromic postfix is found, return the input string concatenated with its reverse
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abba'))  # 'abba'
print(make_palindrome('hello'))  # 'helloolleh'
```