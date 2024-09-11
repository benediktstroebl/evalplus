```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), -1, -1):  # find the longest palindromic postfix
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]  # find the prefix that comes before the palindromic suffix
            return string + prefix[::-1]  # append the reverse of the prefix to the string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcddcba'))  # 'abcddcba'
print(make_palindrome('abcd'))  # 'abcdcba'
```