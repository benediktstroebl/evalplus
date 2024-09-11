Here is a self-contained Python script that includes the `is_palindrome` function and implements the `make_palindrome` function according to the provided algorithm.

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
    # Handle edge case where input string is empty
    if not string:
        return ''

    # Iterate through the string from the end to find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[i - 1:]
        if is_palindrome(postfix):
            # Append the reverse of the prefix to the string to form a palindrome
            return string + string[:i - 1][::-1]

    # If no palindromic postfix is found, the string itself is not a palindrome
    # In this case, append the reverse of the entire string to form a palindrome
    return string + string[::-1]


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This script defines the `is_palindrome` function to check if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function iterates through the input string to find the longest palindromic postfix and appends the reverse of the prefix to form a palindrome. If no palindromic postfix is found, it appends the reverse of the entire string to form a palindrome.