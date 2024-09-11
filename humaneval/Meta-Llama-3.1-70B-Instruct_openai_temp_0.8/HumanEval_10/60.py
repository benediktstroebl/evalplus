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

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):  # find longest postfix that is a palindrome
            return string + string[:i][::-1]  # append reverse of prefix


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcddcba'))  # 'abcddcba'
print(make_palindrome('abcdefgh'))  # 'abcdefghhgfedcba'
```

This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the supplied string that is a palindrome, and then appending the reverse of the prefix that comes before this palindromic suffix. The script includes test cases at the end to demonstrate the functionality of the `make_palindrome` function.