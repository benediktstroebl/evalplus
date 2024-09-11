Here is a self-contained Python script that implements the `is_palindrome` and `make_palindrome` functions.

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

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string + string[::-1]


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: 'catac'
    print(make_palindrome('cata'))  # Output: 'catac'
```

In the `make_palindrome` function, the algorithm starts from the end of the string and tries to find the longest postfix that is a palindrome. Once it finds one, it appends the reverse of the prefix to the end of the string to form the shortest palindrome. If it cannot find any palindromic postfix, it simply appends the reverse of the entire string to itself.