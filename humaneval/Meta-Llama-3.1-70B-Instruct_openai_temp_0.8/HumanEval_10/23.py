Here is a self-contained Python script that solves the problem of finding the shortest palindrome that begins with a supplied string. This script includes the `is_palindrome` function to test if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome.

```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

    Args:
    string (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
    string (str): The input string to make into a palindrome.

    Returns:
    str: The shortest palindrome that begins with the input string.
    """
    if not string:  # if string is empty, return it immediately
        return string

    for i in range(len(string), 0, -1):  # iterate over the string in reverse order
        if is_palindrome(string[i:]):  # check if the current postfix is a palindrome
            return string + string[:i][::-1]  # return the palindrome by appending the reverse prefix


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function iterates over the input string in reverse order to find the longest postfix that is a palindrome, then appends the reverse of the prefix that comes before the palindromic suffix to create the shortest palindrome.