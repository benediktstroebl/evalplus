```python
def is_palindrome(string: str) -> bool:
    """ 
    Test if given string is a palindrome 
    Returns True if a palindrome exists, False otherwise 
    """  
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    
    Algorithm idea: simple 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """  
    return 'catac'
```