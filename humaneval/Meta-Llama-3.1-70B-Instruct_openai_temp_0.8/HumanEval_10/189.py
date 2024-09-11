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

    length = len(string)
    # Find the longest postfix that is a palindrome
    for i in range(length, 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-i]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script provides a solution to the problem of finding the shortest palindrome that begins with a supplied string. The `is_palindrome` function checks whether a string is a palindrome, and the `make_palindrome` function uses this helper function to find the shortest palindrome. The algorithm first finds the longest postfix of the supplied string that is a palindrome, and then appends to the end of the string the reverse of a string prefix that comes before the palindromic suffix. The script includes test cases to verify the correctness of the solution.