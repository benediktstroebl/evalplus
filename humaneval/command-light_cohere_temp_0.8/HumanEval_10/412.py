Here is a Python script that contains a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return string

def not_palindrome(string):
    return bool(is_palindrome(string))
```
The above code defines three functions: is_palindrome checks if a given string is a palindrome; make_palindrome finds the shortest palindrome that begins with a supplied string; and finally, not_palindrome verifies if a given string is a palindrome.