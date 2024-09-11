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

    rev_str = string[::-1]
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + rev_str[i:]


# Test cases
if __name__ == "__main__":
    test_strings = ["", "cat", "cata"]
    for s in test_strings:
        print(f"Original string: {s}")
        print(f"Shortest palindrome: {make_palindrome(s)}")
        print()
```

This script starts with your `is_palindrome` function for testing if a string is a palindrome, then implements the `make_palindrome` function according to the provided algorithm. The test cases cover an empty string and two different palindromes. It prints the original string, the shortest palindrome found for the string and a newline at the end of each test case.