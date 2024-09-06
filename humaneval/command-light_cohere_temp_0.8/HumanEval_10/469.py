```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[1:])

def not_palindrome(string):
    return is_palindrome(string) and make_palindrome(string) == string
```
Do you want me to help you with any other code related problems?