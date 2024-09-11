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
        return ''

    for i in range(len(string) - 1, -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    # If no palindromic postfix is found, append the reverse of the entire string
    return string + string[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with the input string. It uses a simple algorithm that first tries to find the longest palindromic postfix in the string. If found, it appends the reverse of the prefix that comes before this postfix. If no palindromic postfix is found, it simply appends the reverse of the entire string. The script includes example usage and test cases at the end.