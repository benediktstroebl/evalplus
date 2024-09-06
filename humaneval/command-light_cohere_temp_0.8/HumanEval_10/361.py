Here is a Python script that solves the problem of converting a given string into a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Find the longest postfix of the string that is a palindrome
    palindromic = string[:string.rlen(palindrome)]
    reversed_palindrome = string[-palindromic:]
    return string + reversed_palindrome
```

The `is_palindrome` function returns `True` if the given string is a palindrome, and `False` otherwise. The `make_palindrome` function uses a similar algorithm idea to create the palindrome.