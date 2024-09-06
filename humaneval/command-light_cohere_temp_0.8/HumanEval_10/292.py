Here is a Python script that includes a self-contained function that solves the problem of making a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    # Algorithm idea simple: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return ''.join(string[::-1], string[::-1].reverse())
```

This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` creates a palindrome from a given string. The `make_palindrome` function uses a simple algorithm to construct a palindrome, where it finds the longest palindrom substring of the input and reverses it to form the palindrome.