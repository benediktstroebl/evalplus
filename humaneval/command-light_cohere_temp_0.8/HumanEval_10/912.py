```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string
    for char in string[::-1]:
        if palindrome[-1] != char and palindrome[-1].isalnum():
            palindrome = palindrome[:-len(palindrome) - 1] + char
            break

    return palindrome
```
Do you have any other questions related to Python programming or specific use cases?