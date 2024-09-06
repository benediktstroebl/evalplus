```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.joinend(string[:-len(string)//2], string[::-1])
```

This script defines a function that checks if a given string is a palindrome and another that constructs a palindrome from a given string.