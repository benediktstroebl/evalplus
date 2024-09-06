```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[::-1] + string
    return palindrome
```
The is_palindrome function checks if the input string is a palindrome. If it is not, the make_palindrome function constructs a new string that is a palindrome, then returns the palindrome string.