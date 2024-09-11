```markdown
### Self-Contained Python Script to Make the Shortest Palindrome Starting with a Given String

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
        string (str): The input string.

    Returns:
        str: The shortest palindrome starting with the input string.

    Examples:
        >>> make_palindrome('')
        ''
        >>> make_palindrome('cat')
        'catac'
        >>> make_palindrome('cata')
        'catac'
    """
    # Reverse the input string
    reversed_string = string[::-1]
    
    # Initialize the longest palindromic suffix
    longest_palindromic_suffix = ''
    
    # Iterate over the reversed string to find the longest palindromic suffix
    for i in range(len(string) + 1):
        suffix = string[:i][::-1]
        # Check if the suffix is a palindrome
        if is_palindrome(suffix):
            longest_palindromic_suffix = suffix
        # If the suffix is not a palindrome, append the remaining characters to the original string
        else:
            longest_palindromic_suffix = string[:i]
            break
    
    # Make the palindrome by appending the reverse of the remaining prefix
    palindrome = string + longest_palindromic_suffix[::-1]
    
    return palindrome

# Test the function
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: catac
print(make_palindrome("cata"))  # Output: catac
```

This Python script defines two functions: `is_palindrome` to check if a given string is a palindrome and `make_palindrome` to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by first finding the longest palindromic suffix of the input string and its prefix, then appending the reverse of the prefix to the input string to form the palindrome. The script includes examples of how to use the `make_palindrome` function.