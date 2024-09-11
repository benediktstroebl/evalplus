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
    if not string:  # if string is empty
        return ''

    # Reverse the string
    rev_string = string[::-1]

    # Find the longest common prefix between the original string and its reverse
    for i in range(len(string), -1, -1):
        if is_palindrome(string + rev_string[i:]):
            return string + rev_string[i:]


# Test Cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abba'))  # 'abba'
print(make_palindrome('abcddcba'))  # 'abcddcba'
```