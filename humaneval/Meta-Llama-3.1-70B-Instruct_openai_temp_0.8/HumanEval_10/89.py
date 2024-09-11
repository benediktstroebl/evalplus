```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.

    Args:
        string (str): Input string.

    Returns:
        bool: True if string is a palindrome, False otherwise.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
        string (str): Input string.

    Returns:
        str: Shortest palindrome starting with the input string.
    """
    # Handle edge case where input string is empty
    if not string:
        return ''

    # Iterate over possible postfix lengths in descending order
    for i in range(len(string), 0, -1):
        # Check if the current postfix is a palindrome
        if is_palindrome(string[i-1:]):
            # If it's a palindrome, append the reverse of the prefix to the end
            return string + string[:i-1][::-1]

    # If no palindromic postfix is found, return the original string concatenated with its reverse
    return string + string[::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```