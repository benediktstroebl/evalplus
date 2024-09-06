```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ""
    
    is_palindrome_str = is_palindrome(string)
    prefix = is_palindrome_str[:0]
    
    if prefix == string:
        return prefix
    
    suffix = is_palindrome_str[-1:]
    return prefix + suffix[::-1]
```
The function `make_palindrome` takes a string as input and returns the shortest palindrom of the string. It checks if the first checks if the string is empty, and returns an empty string. Then, it checks if the string is equal to its reverse. If yes, it has a palindrome and returns the original string. If no, it finds the longest postfix of the string that is a palindrome and returns it.