Here is a Python script that contains a self-contained function to solve the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    if not string:
        return ""
    if not is_palindrome(string[:len(string)//2]):
        return make_palindrome(string[:len(string)//2]) + string[-len(string)//2:]
    return make_palindrome(string)
```
This script defines a function `make_palindrome` that aims to create the shortest palindrome using the idea of appending a palindrome prefix and a suffix. It also includes a tests to verify the functionality of the `make_palindrome` function.