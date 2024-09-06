```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1] 

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string.
    if not string: 
        return ''
    palindrome = ''
    for char in string:
        if char == palindrome[-1]: 
            palindrome += char
        else: 
            palindrome = char + palindrome[::-1] + char
    return palindrome[::-1]
```
This Python script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, returning `True` if it is, and `False` otherwise. The `make_palindrome` function computes the shortest palindrome that begins with a given string.

The `make_palindrome` function iterates through the characters of the given string. It creates an new palindrome by appending the last character of the string to the reverse of the prefix string.