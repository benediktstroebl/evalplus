```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    palindrome = ""
    while True:
        if is_palindrome(string[-1:]):
            palindrome += string[:-1].reverse(string[:-1])
        break
        palindrome += string[-1]
    return palindrome
```
The function `is_palindrome` checks if a given string is a palindrome. The function `make_palindrome` uses this check and creates a palindrome from the shortest palindrome prefix of the string.