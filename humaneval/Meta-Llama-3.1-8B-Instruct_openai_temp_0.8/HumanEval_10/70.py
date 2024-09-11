### Make Palindrome Function
#### Python Script to Find the Shortest Palindrome That Begins with a Supplied String

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

    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and is_palindrome(string[i:]):
        i += 1
    prefix = string[:i]
    postfix = string[i:]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    reversed_prefix = prefix[::-1]
    return string + reversed_prefix


if __name__ == "__main__":
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # catac
    print(make_palindrome("cata"))  # catac
```

This Python script defines two functions: `is_palindrome` to check if a string is a palindrome, and `make_palindrome` to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the supplied string that is a palindrome, and then appends the reverse of the string prefix that comes before the palindromic suffix.