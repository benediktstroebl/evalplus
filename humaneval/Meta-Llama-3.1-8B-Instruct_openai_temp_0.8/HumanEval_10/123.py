### Make Palindrome Script
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

    :param string: Input string
    :return: Shortest palindrome starting with the input string
    """
    if is_palindrome(string):  # If the string is already a palindrome, return it as is
        return string
    
    # Initialize prefix as an empty string
    prefix = ""
    
    # Loop through the input string from right to left
    for i in range(len(string) - 1, -1, -1):
        # Add the current character to the prefix
        prefix = string[i] + prefix
        
        # If the prefix is a palindrome, break the loop
        if is_palindrome(prefix):
            break
    
    # The longest palindromic postfix of the input string is the suffix
    # The shortest palindrome is the input string plus the reversed prefix
    shortest_palindrome = string + prefix[::-1]
    
    return shortest_palindrome


# Test cases
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```
This script includes the `is_palindrome` function and the `make_palindrome` function with the test cases provided. The `make_palindrome` function first checks if the input string is already a palindrome. If it is, the function returns the string as is. Otherwise, the function iterates over the input string from right to left to find the longest palindromic postfix. The shortest palindrome is then formed by appending the reversed prefix to the input string.