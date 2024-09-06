```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome_str = string + string[::-1]
    while palindrome_str[0] != palindrome_str[1]:
        palindrome_str = palindrome_str[1:] + palindrome_str[:0]
    
    return palindrome_str
```