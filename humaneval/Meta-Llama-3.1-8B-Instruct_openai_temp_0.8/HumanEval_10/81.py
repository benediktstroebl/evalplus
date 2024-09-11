```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:  # edge case for empty string
        return ''

    for i in range(len(string), 0, -1):  # iterate over possible palindrome lengths from longest to shortest
        suffix = string[-i:]  # get the suffix of current length
        if is_palindrome(suffix):  # if suffix is palindrome, it's the longest one we can get
            prefix = string[:-i]  # get the prefix
            return string + prefix[::-1]  # return the palindrome by appending the reversed prefix


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

Note that the `is_palindrome` function is still kept for completeness, but it's not used directly in the `make_palindrome` function. The `make_palindrome` function uses a simple iterative approach to find the longest palindromic suffix of the input string and then appends the reversed prefix to construct the shortest palindrome.