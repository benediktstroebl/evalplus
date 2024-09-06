Here's the self-contained Python function that solves the palindrome problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:0:-1] + string
    return palindrome
```

The function `is_palindrome` checks if a given string is a palindrome, and the function `make_palindrome` generates a palindrome from a given string. The `make_palindrome` function first checks if the input string is already a palindrome, and if not, it constructs the palindrome by removing one character from the beginning and reversing the remaining characters.