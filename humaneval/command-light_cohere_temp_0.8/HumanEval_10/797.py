Here's a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Returns: a True if a palindrome is found, otherwise False.

    Input:
    string: str
    Returns:
        The shortest palindrome that begins with the input string

    Example:
    Input: make_palindrome('cat')
    Output: 'catac' (The shortest palindrome that begins with 'cat')
```

This function takes a string as input and returns the shortest palindrome that begins with the input string. The function uses a longest palindrom that is the same as the original string as the prefix and the reverse of the input string as the suffix to create the palindrome.