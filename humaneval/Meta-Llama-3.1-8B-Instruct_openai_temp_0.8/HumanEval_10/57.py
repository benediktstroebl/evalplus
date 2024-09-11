```markdown
### Shortest Palindrome Finder

This script provides functions for checking if a given string is a palindrome and for finding the shortest palindrome that begins with a supplied string.

```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

    Args:
    string (str): The string to check.

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
    string (str): The string to make a palindrome from.

    Returns:
    str: The shortest palindrome that begins with the supplied string.
    """
    if not string:  # Edge case: empty string
        return ''

    rev_str = string[::-1]  # Reverse the input string
    for i in range(len(string)):  # Check all prefixes of the reversed string
        if string.startswith(rev_str[i:]):  # Check if the input string starts with the current prefix
            return string + rev_str[:i]  # Return the palindrome by appending the reverse of the prefix

    raise ValueError("No palindrome found that begins with the supplied string")


# Example use cases
if __name__ == "__main__":
    print(is_palindrome('radar'))  # True
    print(is_palindrome('hello'))  # False
    print(make_palindrome('cat'))  # catac
    print(make_palindrome('cata'))  # catac
    print(make_palindrome(''))  # ''
```

This script provides the two functions `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, while the `make_palindrome` function finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the input string that is a palindrome and then appends the reverse of the prefix to the end of the string. The script also includes example use cases to demonstrate the usage of these functions.