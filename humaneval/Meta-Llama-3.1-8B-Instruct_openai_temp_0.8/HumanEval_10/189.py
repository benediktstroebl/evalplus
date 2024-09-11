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
    # Find the longest palindrome suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Append the reverse of the prefix to the palindromic suffix
            return string + string[i-1::-1]

    # If no palindrome suffix is found, return an empty string
    return ''


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `is_palindrome` function to check if a string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a given string. It then tests these functions with the provided test cases.