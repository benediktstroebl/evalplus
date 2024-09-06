```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'error: ' + string
    return make_palindrome(substring(string, 1, len(string)//2)) + substring(string, -len(string)//2, len(string)//2)

def substring(string: str, start: int, end: int) -> str:
    return string[start:end+1]

def not_palindrome(string: str) -> bool:
    return make_palindrome(string) == make_palindrome(string)[::-1]
```
This Python code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, returning a boolean result. The `make_palindrome` function computes and returns the shortest palindromic version of a given string. It uses a two helper functions: `substring` extracts a substring from a string, and `not_palindrome` checks if the string is not already a palindrome.