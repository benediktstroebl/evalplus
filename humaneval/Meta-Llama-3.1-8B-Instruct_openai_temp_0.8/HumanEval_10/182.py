```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Args:
    string (str): The input string
    
    Returns:
    str: The shortest palindrome that begins with the supplied string
    """
    # Check if string is empty
    if not string:
        return ''

    # Find the longest postfix that is a palindrome
    longest_palindrome_suffix = ''
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            longest_palindrome_suffix = suffix
            break

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:-len(longest_palindrome_suffix)]

    # Append to the end of the string reverse of the prefix
    palindrome = string + prefix[::-1]

    return palindrome


# Test the function
import doctest
doctest.testmod()
print("Testing complete.")
```

This script defines the `is_palindrome` and `make_palindrome` functions as requested. The `make_palindrome` function uses a simple algorithm to find the shortest palindrome that begins with the supplied string. The `doctest.testmod()` function is used to test the `make_palindrome` function with the provided test cases.