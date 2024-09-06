```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    prefix = string[: len(string) // 2]
    suffix = string[-len(string) // 2:]

    return prefix + suffix[::-1]
```

This code has a function `is_palindrome` that checks if a given string is a palindrome. The function `make_palindrome` takes a string as input and uses the `is_palindrome` function to create the shortest palindrome. 

It first checks if the input string is already a palindrome, and if not, it constructs a palindrome using the `is_palindrome` function.