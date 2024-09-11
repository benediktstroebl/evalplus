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

    # Find the longest palindromic suffix
    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            return string + string[i:][::-1]


def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'


if __name__ == "__main__":
    test_make_palindrome()
    print("All test cases pass")
```

This script includes the `is_palindrome` function to check if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `test_make_palindrome` function is used to test the `make_palindrome` function with different inputs.