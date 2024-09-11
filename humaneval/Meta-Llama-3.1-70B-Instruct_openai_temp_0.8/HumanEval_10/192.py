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
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            # find the longest palindromic suffix
            suffix = string[i:]
            # find the prefix that comes before the palindromic suffix
            prefix = string[:i]
            # reverse the prefix and append it to the end of the string
            return string + prefix[::-1]

    # if no palindromic suffix is found, the entire string is reversed and appended
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('abcddcba'))  # Expected output: 'abcddcba'
print(make_palindrome('abcd'))  # Expected output: 'abcdcba'
```