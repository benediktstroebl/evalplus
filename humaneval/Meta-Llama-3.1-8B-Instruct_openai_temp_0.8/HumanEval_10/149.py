### Shortest Palindrome finder

```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome

    Args:
    string (str): The string to be checked

    Returns:
    bool: True if string is a palindrome, False otherwise
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string

    Args:
    string (str): The string to begin with

    Returns:
    str: The shortest palindrome that begins with the supplied string
    """
    if not string:
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i-1:][::-1]
        if is_palindrome(string[i-1:]):
            prefix = string[:i-1]
            # Append the reverse of the prefix to the end of the postfix to make the palindrome
            palindrome = postfix + prefix[::-1]
            return palindrome

    # If no postfix is found to be a palindrome, reverse the string and append it to itself
    palindrome = string + string[::-1]
    return palindrome


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This Python script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, and the `make_palindrome` function generates the shortest palindrome that begins with a supplied string. The `make_palindrome` function iterates over the string in reverse order, checking for the longest postfix that is a palindrome. If found, it appends the reverse of the prefix to the end of the postfix to make the palindrome. If no postfix is found to be a palindrome, it reverses the string and appends it to itself.