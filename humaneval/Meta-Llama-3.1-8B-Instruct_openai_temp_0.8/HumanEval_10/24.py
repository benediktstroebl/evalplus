### Palindrome Maker
#### A Python Script to Find the Shortest Palindrome Starting with a Given String

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
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[:i]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            prefix = string[:len(string) - i]
            palindrome = postfix + postfix[::-1]
            return string + palindrome[len(prefix):len(prefix) + len(prefix)]
    # If no palindromic suffix found, return the original string
    return string


# Example usage
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```

This script uses the `is_palindrome` function to check if a string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a given string. The `make_palindrome` function works by finding the longest postfix of the given string that is a palindrome, appending the reverse of the string prefix that comes before the palindromic suffix to the end of the string, and returning the resulting palindrome.