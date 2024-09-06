I have implemented the provided function to solve the problem of creating a palindrome from a given string. 
```python
def make_palindrome(string):
    """
    Find the shortest palindrome that begins with the supplied string.
    Algorithm idea simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    
    Returns a standard palindrome by concatenating the prefix and suffix with a common boundary character.
    
    Returns a need palindrome of the supplied string.
    """
    string = ''.join(string)
    return string + string[::-1]
```