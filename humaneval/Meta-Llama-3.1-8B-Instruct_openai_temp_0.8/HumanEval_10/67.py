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
    def is_palindrome_suffix(s: str) -> int:
        """ Helper function to find the length of the longest palindromic suffix """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i]!= s[j]:
                return j - i - 1
            i += 1
            j -= 1
        return j - i + 1

    palindromic_suffix_len = is_palindrome_suffix(string)
    prefix = string[:palindromic_suffix_len]
    palindrome_suffix = string[palindromic_suffix_len:]
    return prefix + palindrome_suffix + prefix[::-1]


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(''))
    print(make_palindrome('cat'))
    print(make_palindrome('cata'))
```

This script defines the `is_palindrome` and `make_palindrome` functions as specified. The `make_palindrome` function now includes a helper function `is_palindrome_suffix` to efficiently find the length of the longest palindromic suffix of the input string. The script also includes example usage to demonstrate the functionality.