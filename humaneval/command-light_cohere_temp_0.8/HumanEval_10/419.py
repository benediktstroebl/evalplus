```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return _make_palindrome(string)
    return string

def _make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return string
    return make_palindrome(string[::-1:]) + string[-1:]

def not_palindrome(string):
    return make_palindrome(string)
```

The code provides a solution to the problem of determining whether a given string is a palindrome and creating the shortest palindrome for an input string that doesn't pass the palindrome test.