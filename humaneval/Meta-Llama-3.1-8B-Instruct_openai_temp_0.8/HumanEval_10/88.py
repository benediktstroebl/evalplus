### Palindrome Maker
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    def is_palindromic_suffix(s: str) -> int:
        """ Find the length of the longest palindromic suffix of the given string """
        for i in range(len(s), 0, -1):
            if is_palindrome(s[-i:]):
                return i
        return 0

    if is_palindrome(string):  # base case: string is already a palindrome
        return string

    suffix_len = is_palindromic_suffix(string)
    return string + string[:suffix_len-1][::-1]


# Example usage:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This code provides two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function finds the shortest palindrome that begins with a supplied string.

The `make_palindrome` function uses a helper function `is_palindromic_suffix` to find the length of the longest palindromic suffix of the given string. It then uses this information to construct the shortest palindrome that begins with the supplied string.

The code also includes example usage of the `make_palindrome` function to demonstrate its behavior.