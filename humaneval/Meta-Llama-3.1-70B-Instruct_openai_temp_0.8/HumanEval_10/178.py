```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome
    
    Args:
        string (str): Input string to check
    
    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Args:
        string (str): Input string to convert into a palindrome
    
    Returns:
        str: The shortest palindrome that begins with the input string
    """
    # Handle edge case of an empty string
    if not string:
        return ''

    # Initialize the longest palindromic suffix to an empty string
    longest_palindromic_suffix = ''

    # Iterate through the string from the end to find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        # Get the current suffix
        suffix = string[i - 1:]

        # Check if the suffix is a palindrome
        if is_palindrome(suffix):
            # If it's longer than the current longest suffix, update the longest suffix
            if len(suffix) > len(longest_palindromic_suffix):
                longest_palindromic_suffix = suffix

    # Find the prefix that comes before the longest palindromic suffix
    prefix = string[:-len(longest_palindromic_suffix)]

    # Append the reverse of the prefix to the end of the string to make a palindrome
    palindrome = string + prefix[::-1]

    return palindrome


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```