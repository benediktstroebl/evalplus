```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
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
        return string

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string + string[::-1]


def main():
    test_cases = [
        ('', ''),
        ('cat', 'catac'),
        ('cata', 'catac'),
    ]

    for string, expected in test_cases:
        result = make_palindrome(string)
        print(f"Test case: '{string}'")
        print(f"Expected: '{expected}'")
        print(f"Actual: '{result}'")
        print(f"Passed: {result == expected}")
        print()


if __name__ == "__main__":
    main()
```