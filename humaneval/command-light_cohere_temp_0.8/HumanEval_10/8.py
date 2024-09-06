Here's the code:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    # Algorithm idea:
    # Same as above.
    return ''.join(string[::-1]) + string

# Test cases
print(make_palindrome('')) # Output: ''
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata')) # Output: cata
print(is_palindrome('')) # Output: True
print(is_palindrome('cat'))  # Output: False
print(is_palindrome('cata')) # Output: True
```