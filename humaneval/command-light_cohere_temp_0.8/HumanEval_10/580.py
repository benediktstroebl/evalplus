```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    l = 0
    while True:
        while l < len(string) - 1 and string[l] == string[l+1]:
            l += 1
        if l == len(string) - 1:
            break
        postfix = string[:l] + string[-l:]
    return postfix + string[::-1]
```
This script provides a function `is_palindrome` that determines if a given string is a palindrome, and a function `make_palindrome` that generates a palindromic string given a prefix.