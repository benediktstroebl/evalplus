```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    prefix = ""
    suffix = string
    while suffix != prefix:
        if is_palindrome(prefix + suffix):
            suffix = suffix[::-1]
        else:
            prefix = prefix + suffix
    return prefix + suffix
```
This code provides a self-contained solution for generating palindromes using a greedy algorithm. It efficiently finds theINP)