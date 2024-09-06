Here's the solution:

```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    prefix = ""
    postfix = string[::-1]
    while postfix[:len(prefix)] != prefix:
        prefix = prefix + postfix
        postfix = postfix[1:]
    return prefix + postfix
```

This solution uses a recursive approach to find the shortest palindrome. It starts with the adding the longest palindrome prefix and postfix of the original string until they match each other. The code is self-contained and efficiently solves the problem of finding the shortest palindrome.