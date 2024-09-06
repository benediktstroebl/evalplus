```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:string.find_palindrome(string[::-1])
    return palindrome + palindrome[::-1]
```
The code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrom that begins with a specified string. 
The `find_palindrome` method is a helper function that recursively searches for the longest palindromic substring within the reversed string. The main `make_palindrome` function works by creating a palindrome from the start and end of the original string and then appending it reversed to itself.