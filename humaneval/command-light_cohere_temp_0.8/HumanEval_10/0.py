Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: return ''
    l = len(string)
    while l:
        p = string[l-1:l]
        if p == p[::-1]:
            return string[:l-1] + p[::-1]
        l -= 1
    return ''
```
The function is_palindrome checks if the given string is a palindrome, and the make_palindrome function finds the shortest palindrome that begins with a supplied string. The function also passes the