```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    """
    # Find the longest palindromic suffix of the string
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Reverse the prefix and append to the palindromic suffix
            return string[:i] + string[:i][::-1]

    # If no palindrome is found, return the original string
    return string


# Testing the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In this code, we use the `is_palindrome` function to check if a given substring is a palindrome. The `make_palindrome` function iterates through the string from the end to find the longest palindromic suffix, reverses the prefix before it, and appends it to form the shortest palindrome that begins with the supplied string.