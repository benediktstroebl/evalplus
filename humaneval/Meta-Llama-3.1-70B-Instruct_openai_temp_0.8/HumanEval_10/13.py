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
        return string

    reversed_string = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(reversed_string[i:] + string):
            return string + reversed_string[:i]
    return string + reversed_string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abccba'))  # 'abccba'
```

The provided script first checks if the input string is empty. If it's not empty, it reverses the string and then iterates from the end of the reversed string. It checks if the current postfix of the reversed string plus the original string forms a palindrome. If it does, it returns the original string plus the remaining prefix of the reversed string. If no such postfix is found, it simply returns the original string plus its reverse.