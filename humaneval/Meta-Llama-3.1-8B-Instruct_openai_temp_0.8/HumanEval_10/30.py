Here's a self-contained Python script that solves the problem:
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

    # Find the longest postfix of supplied string that is a palindrome
    suffix = string
    while suffix and not is_palindrome(suffix):
        suffix = suffix[1:]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(suffix)]
    palindrome = string + prefix[::-1]

    return palindrome


if __name__ == "__main__":
    print("Testing make_palindrome function:")
    print("make_palindrome(''):", make_palindrome(''))
    print("make_palindrome('cat'):", make_palindrome('cat'))
    print("make_palindrome('cata'):", make_palindrome('cata'))
```
This script contains two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, and the `make_palindrome` function generates the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome, and then appending the reverse of the prefix to the end of the string. The script includes test cases to verify the correctness of the `make_palindrome` function.