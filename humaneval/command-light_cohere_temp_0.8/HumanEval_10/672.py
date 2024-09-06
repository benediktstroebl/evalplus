```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    elif len(string) == 1:
        return string
    else:
        # Find the longest postfix of supplied string that is a palindrome
        l = len(string)
        pal = string[::-1][:l-1]
        
        # append to the string reverse of a string prefix that comes before the palindromic suffix
        return pal + string[-1:]l
```