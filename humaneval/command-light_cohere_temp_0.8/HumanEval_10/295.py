```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:0:-1] + string[::-1]
    return palindrome
```
The function `make_palindrome` accepts a string and attempts to generate a palindrome by locating the string's characters. If no palindrome is found, it returns an empty string.