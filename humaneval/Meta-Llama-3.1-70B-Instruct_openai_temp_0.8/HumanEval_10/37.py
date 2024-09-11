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
    # find the longest postfix of string that is a palindrome
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # find the prefix that is not part of the palindrome
            prefix = string[:i]
            # return the string with the prefix reversed appended
            return string + prefix[::-1]

    # if no palindrome is found, return the string reversed
    return string + string[::-1]


if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
```

This script includes the provided `is_palindrome` function and the `make_palindrome` function. The `make_palindrome` function works by iterating over the string from the end to the start, finding the longest postfix that is a palindrome. Once it finds the longest postfix palindrome, it finds the prefix that is not part of the palindrome, reverses the prefix, and appends it to the end of the string. If no palindrome is found, it simply returns the string with itself reversed.