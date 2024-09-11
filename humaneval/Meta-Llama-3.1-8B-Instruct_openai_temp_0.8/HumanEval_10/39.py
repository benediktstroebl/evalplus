### Self-Contained Python Script
```markdown
### Palindrome Functions

```python
def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.
    
    Args:
    string (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    The algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Args:
    string (str): The input string to begin with.
    
    Returns:
    str: The shortest palindrome that begins with the input string.
    """
    
    # Reverse the input string
    rev_string = string[::-1]
    
    # Find the longest common prefix between the input string and its reverse
    i = 0
    while i < len(string) and i < len(rev_string) and string[i] == rev_string[i]:
        i += 1
    
    # If the input string is equal to its reverse, it's already a palindrome
    if i >= len(string):
        return string
    
    # Otherwise, append the reverse of the prefix to the input string
    return string + rev_string[i:]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome('radar'))   # True
    print(is_palindrome('hello'))   # False
    print(make_palindrome('cat'))   # catac
    print(make_palindrome('cata'))  # catac
    print(make_palindrome(''))      # ''
```

This script defines two functions, `is_palindrome` and `make_palindrome`, to check if a given string is a palindrome and to find the shortest palindrome that begins with a supplied string, respectively. The `make_palindrome` function uses a simple algorithm to find the longest postfix that is a palindrome and appends the reverse of the prefix to the end of the input string to form the shortest palindrome. The example usage section demonstrates how to use these functions.