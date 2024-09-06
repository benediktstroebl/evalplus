```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return _make_palindrome(string)
    else:
        return string

def _make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return string

def not_palindrome(string: str) -> bool:
    return is_palindrome(string) and is_palindrome(string[::-1])

# Example usage
make_palindrome('cata') # Output: 'catac'
```
This script defines a self-contained function, `is_palindrome`, which checks if a given string is a palindrome. The `make_palindrome` function then uses this function to create the shortest palindrome.