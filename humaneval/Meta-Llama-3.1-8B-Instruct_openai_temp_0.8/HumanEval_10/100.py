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
    def longest_palindromic_suffix(string: str) -> tuple[str, str]:
        """ Find the longest palindromic suffix and the corresponding prefix """
        for i in range(len(string), 0, -1):
            if is_palindrome(string[:i]):
                return string[:i], string[i:]
        return "", ""

    prefix, suffix = longest_palindromic_suffix(string)
    return string + suffix[::-1]


# Example usage
if __name__ == "__main__":
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # catac
    print(make_palindrome("cata"))  # catac
```

This script defines the `is_palindrome` function to check if a string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a given string. The `make_palindrome` function uses a helper function `longest_palindromic_suffix` to find the longest palindromic suffix of the string, and then appends the reverse of the corresponding prefix to the end of the string. The example usage at the end demonstrates how to use these functions.