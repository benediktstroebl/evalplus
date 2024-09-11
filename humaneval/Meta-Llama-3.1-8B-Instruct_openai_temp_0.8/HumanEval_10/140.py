### Palindrome Maker Script
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
    # Find the longest postfix of supplied string that is a palindrome
    rev_str = string[::-1]
    for i in range(len(string) + 1):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            prefix = string[:i]
            return prefix + postfix + prefix[::-1]

    # If no palindrome postfix found, return the original string
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This script defines the `is_palindrome` function to check if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the supplied string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix to the end of the string. If no palindrome postfix is found, the function returns the original string.