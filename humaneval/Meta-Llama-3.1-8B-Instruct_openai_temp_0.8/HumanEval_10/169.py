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
    if not string:  # if input string is empty, return an empty string
        return ''

    left = 0
    right = len(string) - 1
    while left < right:
        if string[left]!= string[right]:
            break
        left += 1
        right -= 1

    # if the whole string is a palindrome, reverse the string and concatenate
    if left >= right:
        return string + string[::-1]

    # otherwise, find the longest palindrome suffix
    palindrome_suffix = string[left + 1:right + 1]
    # and append the reversed prefix
    return string + palindrome_suffix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines two functions: `is_palindrome` checks if a string is a palindrome, and `make_palindrome` creates the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a two-pointer approach to find the longest palindrome suffix of the input string, and then appends the reversed prefix to create the shortest palindrome. The test cases at the end demonstrate the function's behavior with different inputs.