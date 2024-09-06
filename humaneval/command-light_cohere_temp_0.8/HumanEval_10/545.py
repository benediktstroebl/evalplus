Here is a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    return ''.join(c for c in string if c.isalpha()) + [(reversed(string[:-len(c)]) + string[len(c):]]
```
This function uses a list comprehension to filter out non-alph strings and a list method to reverse the string. The function then creates the string with the reversed prefix and appends it to the original string.