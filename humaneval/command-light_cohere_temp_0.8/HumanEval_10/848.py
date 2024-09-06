```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string.
    if not string: 
        return ''
    palindrome = ''
    for i, char in enumerate(string):
        if is_palindrome(char):
            palindrome += char
        else: 
            palindrome = char + palindrome[::-1] 
    return palindrome[::-1]
```