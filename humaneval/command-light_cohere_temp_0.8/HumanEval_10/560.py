```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''
    
    palindrome = ''
    reverse_prefix = string[::-1]
    while reverse_prefix in palindrome:
        palindrome += reverse_prefix
        reverse_prefix = string[::-1]
    return palindrome
```