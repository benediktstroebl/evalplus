```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ""
    
    palindrome = []
    while True:
        palindrome.append(char if char in string and char == string[0] or char == string[-1])
        string = string[1:]
    if not string:
        break
    return palindrome[::-1]
```
The code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` finds and returns the shortest palindrom that begins with the given string. 

The algorithm works by trying every character in the string and keeping track of whether the palindrome has been built so far. The loop continues until no more palindrome can be built.