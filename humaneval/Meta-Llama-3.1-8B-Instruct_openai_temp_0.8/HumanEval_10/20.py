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
    def longest_palindromic_suffix(string: str) -> str:
        """ Find the longest palindromic suffix of a given string """
        for i in range(len(string), 0, -1):
            if is_palindrome(string[-i:]):
                return string[-i:]

    # Find the longest palindromic suffix
    palindromic_suffix = longest_palindromic_suffix(string)

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:-len(palindromic_suffix)]

    # Append the reverse of the prefix to the end of the string
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `is_palindrome` function to check if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `longest_palindromic_suffix` helper function is used to find the longest palindromic suffix of a given string. The test cases are included at the end of the script.