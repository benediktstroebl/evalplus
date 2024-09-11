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
        return string

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    return string + string[::-1]


def main():
    # Test cases
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
    print(make_palindrome('abba'))  # 'abba'
    print(make_palindrome('hello'))  # 'helloolleh'


if __name__ == "__main__":
    main()
```

This script uses a helper function `is_palindrome` to check whether a given string is a palindrome. In the `make_palindrome` function, it starts from the end of the input string and checks for the longest palindromic postfix. Once found, it appends the reverse of the prefix before this postfix to the end of the string to form the shortest palindrome that begins with the input string. If no palindromic postfix is found, it appends the reverse of the entire string to itself.