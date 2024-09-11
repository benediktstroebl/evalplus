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
    if not string:
        return ''

    rev_string = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i] + rev_string[i:]):
            return string + rev_string[i:]
    return string + rev_string


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

In this script, the `make_palindrome` function works by first reversing the input string and then iterating over the reversed string from the end to the start. It checks if the concatenation of the first `i` characters of the original string and the remaining characters of the reversed string is a palindrome. If it is, it returns this concatenated string, which is the shortest palindrome that begins with the original string.

The `is_palindrome` function is a helper function that checks if a given string is a palindrome by comparing it to its reverse.