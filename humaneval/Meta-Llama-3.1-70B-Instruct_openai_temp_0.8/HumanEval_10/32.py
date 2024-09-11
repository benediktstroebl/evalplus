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
    if is_palindrome(string):
        return string

    for i in range(len(string) - 1, -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]


def main():
    print(make_palindrome(''))  # Expected output: ''
    print(make_palindrome('cat'))  # Expected output: 'catac'
    print(make_palindrome('cata'))  # Expected output: 'catac'


if __name__ == "__main__":
    main()
```

This script first checks if the input string is a palindrome. If it is, the function returns the string as is. If not, it finds the longest postfix that is a palindrome, and appends the reverse of the prefix before this postfix to the original string. The `main` function tests the `make_palindrome` function with provided test cases.