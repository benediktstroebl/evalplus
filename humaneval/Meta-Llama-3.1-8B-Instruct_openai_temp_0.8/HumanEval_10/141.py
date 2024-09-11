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
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + postfix[::-1]

    # If no palindrome postfix is found, return the original string
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines a function `make_palindrome(string: str) -> str` that returns the shortest palindrome string that begins with the input `string`. It uses a simple algorithm to find the longest palindrome postfix of the input string and appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. If no palindrome postfix is found, it returns the original string.