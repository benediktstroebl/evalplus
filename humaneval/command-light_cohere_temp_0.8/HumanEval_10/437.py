Here's the solution function:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    l = len(string)
    while l > 1 and is_palindrome(string[:l - 1]) and is_palindrome(string[-l:]):
        l -= 1
    return string + string[::-1][l:]
```
This function takes a string as input and returns a boolean value indicating whether the string is a palindrome or not. It also includes a a helper function is_palindrome that checks if a given string is a palindrome or not. The make_palindrome function then loops until it finds the shortest palindrome that begins with the given string.