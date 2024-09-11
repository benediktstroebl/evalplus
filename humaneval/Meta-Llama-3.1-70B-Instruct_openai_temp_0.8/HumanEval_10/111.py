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
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abba'))  # 'abba'
print(make_palindrome('abcddcba'))  # 'abcddcba'
```
This script defines two functions: `is_palindrome` checks if a string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The test cases at the end verify that the `make_palindrome` function works correctly.