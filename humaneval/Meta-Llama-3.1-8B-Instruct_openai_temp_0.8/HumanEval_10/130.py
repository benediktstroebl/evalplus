### Palindrome Maker
#### Python Script

```markdown
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
        return ""

    # Find the longest palindromic suffix of the string
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Append reverse of the prefix to the end of the suffix
            return suffix + string[:-i][::-1]


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ""
    print(make_palindrome("cat"))  # Output: "catac"
    print(make_palindrome("cata"))  # Output: "catac"
```

### Explanation

This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with a supplied string. It does this by finding the longest palindromic suffix of the string, then appends the reverse of the prefix to the end of the suffix.

In the `make_palindrome` function, it iterates over the string from the end to the beginning, checking each suffix to see if it's a palindrome using the `is_palindrome` function. When it finds a palindromic suffix, it computes the reverse of the prefix and appends it to the end of the suffix, returning the resulting palindrome. If the input string is empty, it returns an empty string.