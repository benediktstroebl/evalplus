```python
def is_palindrome(string: str) -> bool:
    """ Check if a given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Create the shortest palindrome for a given string."""
    if not string:
        return ''
    
    # Longest palindromic postfix of the string
    palindrome = []
    for char in string:
        if char == char[::-1]:
            palindrome.append(char)
    
    # Reverse the palindrome and append to the original string
    return string + palindrome[::-1]
```