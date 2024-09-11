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
        return ''

    for i in range(len(string), 0, -1):  # iterate from the end to the start
        postfix = string[i:]  # get the postfix
        if is_palindrome(postfix):  # check if it's a palindrome
            prefix = string[:i]  # get the prefix
            return string + prefix[::-1]  # return the palindrome string

    # if no palindrome postfix is found, append the reverse of the string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

This script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse. The `make_palindrome` function uses this to find the shortest palindrome that begins with a supplied string.

In the `make_palindrome` function, it iterates from the end of the string to the start and checks each postfix to see if it's a palindrome. If it finds a palindrome postfix, it appends the reverse of the prefix to the end of the string and returns it. If it doesn't find any palindrome postfix, it simply appends the reverse of the string to itself.

The script includes test cases at the end to verify that the `make_palindrome` function works correctly.