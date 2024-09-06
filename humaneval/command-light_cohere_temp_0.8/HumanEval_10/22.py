Here's the function:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    return "cat" if is_palindrome("cat") else return "".
```

This function uses a simple algorithm to find the shortest palindrome in a string. It returns the 'cat' if the string passed to the function is a palindrome, and otherwise returns an empty string.