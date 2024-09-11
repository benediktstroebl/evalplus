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
    def find_longest_palindromic_suffix(string):
        """ Find the longest palindromic suffix of the given string """
        for i in range(len(string), -1, -1):
            if is_palindrome(string[i:]):
                return string[:i]
        return ""

    # Find the longest palindromic suffix
    longest_palindromic_suffix = find_longest_palindromic_suffix(string)

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(longest_palindromic_suffix)]

    # Append the reverse of the prefix to the end of the string
    return string + prefix[::-1]


# Test cases
print(make_palindrome(""))  # ''
print(make_palindrome("cat"))  # 'catac'
print(make_palindrome("cata"))  # 'catac'
```

The script defines the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. It uses a helper function `find_longest_palindromic_suffix` to find the longest palindromic suffix of the given string. The test cases are provided at the end of the script to verify the correctness of the function.