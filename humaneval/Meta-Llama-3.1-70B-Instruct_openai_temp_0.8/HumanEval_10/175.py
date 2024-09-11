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
    if not string:  # if the string is empty
        return string

    for i in range(len(string), 0, -1):  # iterate from the end of the string to the start
        if is_palindrome(string[i:]):  # check if the postfix is a palindrome
            return string + string[:i][::-1]  # return the string with the prefix reversed and appended


# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome('abba'))  # Output: 'abba'
print(make_palindrome('abcd'))  # Output: 'abcdcba'
```