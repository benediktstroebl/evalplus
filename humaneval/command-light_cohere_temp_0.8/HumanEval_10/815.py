```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    
    # Longer palindrome first
    # Algorithm idea from above
    pal = string + string[::-1]
    
    return pal
```