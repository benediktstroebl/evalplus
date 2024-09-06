```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    palindrome = string
    
    while palindrome[-1] != palindrome[0]:
        palindrome = palindrome[1:] + palindrome[:-

    return palindrome
```
The function checks if the given string is a palindrome or not. If yes, it returns true; otherwise, it returns false. 

The function then creates a new string that is a palindrome of the original string.