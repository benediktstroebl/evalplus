### Creating the Shortest Palindrome

Here's a Python script that implements the `is_palindrome` and `make_palindrome` functions.

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
    if is_palindrome(string):
        return string

    # Reversed string prefix
    prefix = ''

    # Find the longest postfix of the string that is a palindrome
    i = 0
    while i < len(string):
        # Check if the current postfix of the string is a palindrome
        if is_palindrome(string[i:]):
            # The longest palindrome postfix is found
            break
        i += 1

    # The remaining suffix of the string is a palindrome
    palindrome_suffix = string[i:]

    # The prefix of the string that comes before the palindrome suffix
    prefix = string[:i]

    # The reversed prefix of the string
    reversed_prefix = prefix[::-1]

    # The shortest palindrome is formed by appending the reversed prefix to the palindrome suffix
    return palindrome_suffix + reversed_prefix


# Example usage:
print(is_palindrome('radar'))  # True
print(is_palindrome('python'))  # False
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
```

This Python script implements the `is_palindrome` and `make_palindrome` functions, along with the example usage for testing purposes. The `make_palindrome` function attempts to find the shortest palindrome that begins with a supplied string by identifying the longest postfix of the string that is a palindrome, and then appending the reversed prefix of the string to the palindrome suffix. The `is_palindrome` function checks whether a given string is a palindrome by comparing it with its reverse.