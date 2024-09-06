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
    return make_palindrome(string[::-1:]) + string[:-len(string) // 2])

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))
```
The function `make_palindrome` is a recursive helper that uses `is_palindrome` to create the shortest palindrome. It then uses the ' split the string into a prefix and a postfix, and then calls `make_palindrome` recursively with the prefix and postfix.

To check if a string is a palindrome, we use the helper function `is_palindrome`. The function takes a string as input and returns a boolean value indicating whether the string is a palindrome or not.

This is a simple example of a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a given string.