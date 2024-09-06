The solution has been improved to make it more efficient and readable:
```python
def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    return ''.join(c for c in s if c == s[::-1][idx] for idx in range(len(s)-1, 0, -1))
```

The code defines a function `is_palindrome` that checks if a given string is a palindrome. The `make_palindrome` function uses a list comprehension to create a new string by appending only palindromic characters to the original string.