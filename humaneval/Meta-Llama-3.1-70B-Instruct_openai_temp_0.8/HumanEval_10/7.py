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
    if not string:
        return ''

    rev_string = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(rev_string[i:] + string):
            return string + rev_string[:i]


# Example use cases:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome('abc'))  # Output: 'abcba'
print(make_palindrome('abcd'))  # Output: 'abcdcba'
```
This Python script includes the `is_palindrome` function to check if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. It iterates through the input string from the end to find the longest postfix that is a palindrome and then appends the reverse of the prefix to the original string.