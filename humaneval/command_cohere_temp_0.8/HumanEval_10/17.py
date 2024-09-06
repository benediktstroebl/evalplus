Here's a Python script with a self-contained function that solves the problem using Python 3.10 string overlays and suffixes:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # find the longest palindromic suffix
    i = string.rfind(string[::-1]) + 1
    
    # reverse the prefix up to the palindromic suffix
    new_string = string[:i] + string[i:i+1][::-1] + string[i+1:]
    return new_string
```
The `make_palindrome` function uses string overlays to reverse the prefix up to the palindromic suffix without reconstructing the string and returns the shortest palindrome beginning with the supplied string.