Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''
    palindrome = ''
    reverse = string[::-1]
    while reverse in palindrome:
        palindrome += reverse 
        reverse = string[::-1]
    return palindrome
```
The function `make_palindrome` constructs a palindrome by iteratively appending the reverse of the prefix to the end of the `palindrome` while removing the reverse of the prefix.