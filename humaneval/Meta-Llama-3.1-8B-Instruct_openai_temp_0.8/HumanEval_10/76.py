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
    if len(string) <= 1:  # if string is empty or has one character, it's a palindrome
        return string

    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):  # check if postfix is a palindrome
            return string + postfix[::-1]  # append reverse of prefix to the end of the string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script implements the `make_palindrome` function using a simple iterative approach to find the longest postfix of the string that is a palindrome. The `is_palindrome` function is also implemented to check if a given string is a palindrome. The test cases demonstrate the functionality of the `make_palindrome` function.