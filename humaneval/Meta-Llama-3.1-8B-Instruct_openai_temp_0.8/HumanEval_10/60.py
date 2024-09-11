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
    def find_longest_palindrome_suffix(string: str) -> int:
        """ Find length of the longest suffix of string that is a palindrome """
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left]!= string[right]:
                return left
            left += 1
            right -= 1
        return left

    suffix_length = find_longest_palindrome_suffix(string)
    palindrome_suffix = string[suffix_length:]
    palindrome_suffix_reverse = palindrome_suffix[::-1]

    if suffix_length == 0:
        # The string itself is a palindrome
        return string + string
    else:
        # Append the reverse of the prefix to the palindromic suffix
        return string + palindrome_suffix_reverse


# Test the function
if __name__ == "__main__":
    print(make_palindrome(''))
    print(make_palindrome('cat'))
    print(make_palindrome('cata'))
    print(make_palindrome('radar'))
```

This script defines the `is_palindrome` function to check if a string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `find_longest_palindrome_suffix` helper function is used to find the length of the longest suffix of the string that is a palindrome. The `make_palindrome` function uses this information to construct the shortest palindrome that begins with the supplied string.

In the test section, the script prints the result of `make_palindrome` for several test cases.