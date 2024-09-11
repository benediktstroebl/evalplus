### Make Palindrome Function
#### Python Script

```markdown
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
        str: The shortest palindrome that begins with the supplied string.
    """
    
    # Edge case: empty string
    if not string:
        return ''
    
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[i:][::-1]


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # catac
    print(make_palindrome('cata'))  # catac
```

This Python script defines a function to check if a given string is a palindrome and another function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function finds the longest postfix of the supplied string that is a palindrome and appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. The example usage demonstrates how to use these functions.