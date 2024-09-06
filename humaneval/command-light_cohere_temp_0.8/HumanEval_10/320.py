```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ''
    # Find the longest postfix of supplied string that is a palindrome
    l = len(string)
    while True:
        sp = string[l-1:l]
        if sp == sp[::-1]:
            return string[:l-1]+string[l:]
        l = len(sp)
```
The function 'make_palindrome' finds the shortest palindrome by iteratively searching for the longest postfix of the given string that is also a palindrome.