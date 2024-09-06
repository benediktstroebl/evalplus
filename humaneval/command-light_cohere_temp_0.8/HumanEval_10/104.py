```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0:-1] + string
    return palindrome

def not_palindrome(text):
    assert is_palindrome(text)
    return make_palindrome(text)
```

The code defines a function `is_palindrome` that checks if a given string is a palindrome and another function `make_palindrome` that finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses the `is_palindrome` to first check if a palindrome exists in the string. Then it proceeds to create a palindrome by removing one character from the beginning and adding the rest of the characters in reverse.