```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ""

    # Find the longest palindrome that begins with the string.
    while True and is_palindrome(string[:len(string) - 1]):
        string = string[:len(string) - 1] + string[::-1]
    return string
```
This code defines a function is_palindrome that checks if a given string is a palindrome. The make_palindrome function takes a string as input and uses a helper function is_palindrome to determine if the string is a palindrome, and then constructs the palindrome using the result of is_palindrome.