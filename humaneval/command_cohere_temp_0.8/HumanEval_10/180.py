Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    i = string.rfind(''.join(reversed(string[:-1]))):
    
    # Reverse the prefix up to the palindromic suffix
    new_string = string[:i] + string[i:][::-1]
    
    return new_string
```