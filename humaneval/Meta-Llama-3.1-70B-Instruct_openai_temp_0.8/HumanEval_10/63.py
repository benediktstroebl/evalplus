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
    if not string:  # if string is empty, return empty string
        return string

    for i in range(len(string), 0, -1):  # find the longest postfix that is a palindrome
        if is_palindrome(string[i-1:]):
            postfix = string[i-1:]
            prefix = string[:i-1]
            return string + prefix[::-1]  # return the shortest palindrome


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('race'))  # 'racecar'
```

In this script, the `is_palindrome` function checks whether a given string is a palindrome by comparing it to its reverse.

The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome. It then appends the reverse of the prefix that comes before this palindromic suffix to the end of the input string. This results in the shortest palindrome that begins with the input string.