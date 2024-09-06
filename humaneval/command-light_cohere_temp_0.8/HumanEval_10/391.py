```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindromic_start = next((i for i, char in enumerate(string) if char == char[::-1]), None)
    if palindromic_start is None:
        return string

    result = string[:palindromic_start] + string[-palindromic_start:]
    return result
```

This code defines two functions: is_palindrome and make_palindrome. The is_palindrome function checks if a given string is a palindrome. The make_palindrome function constructs a palindrome using the idea of finding the longest palindromic substring within a given string.