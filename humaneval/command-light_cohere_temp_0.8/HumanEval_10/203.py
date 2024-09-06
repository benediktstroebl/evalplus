```python
def is_palindrome(string: str) -> bool:
    """ Check if a given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Create a palindrome from a non-palindrome string."""
    if not palindrome := len(string) and all(c for c in string if c == string[1-i]) or not string:
        return palindrome = ''.join(reversed(string))
    return palindrome
```