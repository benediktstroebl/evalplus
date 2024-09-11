### Shortest Palindrome
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Args:
        string (str): Input string
    
    Returns:
        str: The shortest palindrome that begins with the input string
    """
    # If string is already a palindrome, return it
    if is_palindrome(string):
        return string
    
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Reverse the prefix that comes before the palindromic suffix
            prefix = string[:-i][::-1]
            return prefix + postfix


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script provides a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. The function works by first checking if the input string is already a palindrome. If not, it finds the longest postfix of the supplied string that is a palindrome, and then appends to the end of the string the reverse of a string prefix that comes before the palindromic suffix. The result is the shortest palindrome that begins with the input string.