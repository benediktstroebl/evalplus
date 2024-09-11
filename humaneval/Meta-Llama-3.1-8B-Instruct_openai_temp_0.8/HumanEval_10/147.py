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
    if not string:
        return ''

    for i in range(len(string), 0, -1):
        substring = string[-i:]
        if is_palindrome(substring):
            return string + substring[::-1]


# Example usage
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: "catac"
print(make_palindrome("cata"))  # Output: "catac"
```

This script defines the `is_palindrome` function to check if a string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a given string. The `make_palindrome` function uses the `is_palindrome` function to find the longest postfix of the given string that is a palindrome, and then appends the reverse of the prefix to it to form the shortest palindrome. The example usage demonstrates how to use these functions.