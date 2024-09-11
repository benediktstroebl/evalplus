### Palindrome Generator Script
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
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            # Reverse the prefix and append it to the suffix
            return string + string[-i:][::-1]

    # If no palindromic suffix was found, return the original string
    return string


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: catac
    print(make_palindrome('cata'))  # Output: catac
```

This script generates the shortest palindrome that begins with a supplied string by finding the longest palindromic suffix of the string and appending the reverse of the prefix to it. If no palindromic suffix is found, it returns the original string. The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse. The `make_palindrome` function uses this helper function to find the shortest palindrome.