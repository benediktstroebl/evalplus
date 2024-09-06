The following Python code is a self-contained function that solves the problem of finding the shortest palindrome that begins with a given string. 

```python
def is_palindrome(string): 
        """ Test if given string is a palindrome """
        return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with the supplied string.
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    string = ''.join(string) + string[::-1]
    return string
```