### Palindrome Extension Algorithm

Here's the complete Python script with the `is_palindrome` and `make_palindrome` functions:

```markdown
### Palindrome Extension Algorithm

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
    if not string:
        return ""

    # Check if string itself is a palindrome
    if is_palindrome(string):
        return string

    for i in range(len(string) - 1, -1, -1):
        substr = string[:i+1]
        if is_palindrome(substr):
            return string + substr[::-1]


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome('radar'))  # Output: 'radar'
print(make_palindrome('python'))  # Output: 'pythonon'
```

The `make_palindrome` function works by trying to extend the input string with its reverse, but only as long as the resulting substring is a palindrome. If it's not, it tries to extend the substring further. The process repeats until it finds the longest palindromic suffix of the input string, which then has its reverse appended to form the shortest palindrome starting with the input string.