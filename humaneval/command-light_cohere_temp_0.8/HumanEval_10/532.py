```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string.
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return ''.join(string[::-1] + string)
```