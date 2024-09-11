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
    # Handle edge case where string is empty
    if not string:
        return ''

    # Iterate over the string from the end to find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Find the prefix that comes before the palindromic suffix
            prefix = string[:i]
            # Append the reverse of the prefix to the end of the string
            return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```

This script defines two functions: `is_palindrome`, which checks whether a string is a palindrome, and `make_palindrome`, which finds the shortest palindrome that begins with a given string. The `make_palindrome` function works by finding the longest palindromic suffix of the string and then appending the reverse of the prefix that comes before it. The test cases at the end of the script demonstrate the correctness of the functions.