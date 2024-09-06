This is a self-contained Python function that solves the problem of converting a given string into a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''
    
    str_prefix = str(string)
    str_palindrome = str_prefix + str_prefix[::-1]
    
    return str_palindrome
```
This function uses the algorithm to create the shortest palindrome by adding the reverse of the prefix. It uses a string prefix and the string prefix itself to create the palindrome.