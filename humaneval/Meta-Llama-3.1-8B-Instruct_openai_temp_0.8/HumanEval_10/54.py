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
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            prefix = string[:-i]
            return string + prefix[::-1]

    raise ValueError("This function should never be called.")


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
    print(make_palindrome('aba'))  # 'ababa'
```
This code defines two functions: `is_palindrome` and `make_palindrome`. The `make_palindrome` function works by trying postfixes of decreasing length, checking if they're palindromes, and if so, returns the shortest palindrome by appending the reverse of the prefix to the end of the postfix.