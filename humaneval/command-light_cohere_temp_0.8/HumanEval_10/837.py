```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:len(string)//2]
    return palindrome + palindrome[::-1]
```
The is_palindrome function checks if the given string is a palindrome, and the make_palindrome function constructs a palindrome from the input string.