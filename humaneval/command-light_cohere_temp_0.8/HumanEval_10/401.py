```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ''
    palindrome = ''
    while True:
        x = string[0]
        for char in string[1:]:
            if x == char and is_palindrome(string[::-1]) == True:
                break
            palindrome = palindrome + char
        else:
            break
    return palindrome
```
The function is_palindrome checks if a given string is a palindrome or not, and the make_palindrome function uses the algorithm to create the shortest palindrom that begins with the supplied string.