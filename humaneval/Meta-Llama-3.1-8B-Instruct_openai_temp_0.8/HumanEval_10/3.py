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
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            prefix = string[:-i]
            return prefix + postfix + prefix[::-1]

    # If no palindromic postfix is found, return the original string
    return string


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
    print(make_palindrome('abcd'))  # 'abdcba'
```

This Python script defines the `is_palindrome` and `make_palindrome` functions as specified in the problem statement. The `make_palindrome` function iterates through the string to find the longest postfix that is a palindrome and then constructs the shortest palindrome that begins with the supplied string by appending the reverse of the string prefix that comes before the palindromic suffix.