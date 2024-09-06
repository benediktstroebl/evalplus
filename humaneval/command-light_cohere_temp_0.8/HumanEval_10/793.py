Here is a self-contained Python function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        palindrome = string[:len(string) // 2] + string[-len(string) // 2:]
        return palindrome
```

This function, `is_palindrome`, checks if a given string is a palindrome. The function `make_palindrome` uses this check to create the shortest palindrome that begins with the supplied string.