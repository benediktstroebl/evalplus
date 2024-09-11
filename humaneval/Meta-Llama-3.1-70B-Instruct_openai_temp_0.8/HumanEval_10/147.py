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
    if not string:  # Edge case: empty string
        return ''

    for i in range(len(string), 0, -1):  # Iterate over possible postfix lengths
        postfix = string[-i:]  # Get the postfix
        if is_palindrome(postfix):  # Check if postfix is a palindrome
            prefix = string[:-i]  # Get the prefix
            return string + prefix[::-1]  # Append reverse of prefix to the string

    # If no palindromic postfix is found, the whole string is not a palindrome
    return string + string[::-1][1:]  # Remove the middle character if the string has odd length


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This Python script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks whether a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that begins with a given string. The algorithm used is based on finding the longest palindromic postfix of the input string and appending the reverse of the prefix that comes before the palindromic suffix. The script also includes test cases to verify the correctness of the `make_palindrome` function.