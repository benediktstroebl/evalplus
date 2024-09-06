Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[1:]
    i = 2
    while len(palindrome) < len(string):
        if palindrome[-1] == palindrome[0]:
            palindrome = palindrome[1:] + string[i:][::-1]
            i += 1
        else:
            palindrome = palindrome[0:] + string[i:][::-1]
            i += 1
    
    return palindrome[::-1]
```
The above code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, returning a boolean value. The `make_palindrome` function computes the shortest palindrome that begins with the given string.