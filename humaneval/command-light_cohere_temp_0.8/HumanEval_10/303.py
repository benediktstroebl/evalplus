```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ""
    elif string == '': 
        return ''
    else:
        # Find the longest postfix of supplied string that is a palindrome
        palindrome = string[::-1].join(string)
        return palindrome
```