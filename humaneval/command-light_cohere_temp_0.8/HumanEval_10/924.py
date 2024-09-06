```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    
    palindrome = []
    i = 0
    while i < len(string):
        if is_palindrome(string[i:]) or i == len(string) - 1:
            break
        palindrome.append(string[i])
        palindrome.reverse()
       her reverse() string[:i+1]
    return ''.join(palindrome)
```