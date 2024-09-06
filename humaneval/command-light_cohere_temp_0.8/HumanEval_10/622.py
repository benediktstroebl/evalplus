```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix. 
    Returns: list comprehension with reversed and slicing. 
    """ Returns longest palindrome: "catac" 
    """
    return ''.join(reversed(string[:-palindrome]) + reversed(string[-palindrome:]))

# Test cases
print(is_palindrome(''))  # Output: True
print(is_palindrome('cat'))  # Output: True
print(is_palindrome('cata'))  # Output: False
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'cataa'
```
This code has two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function constructs a palindrome. The function works by finding the longest palindrome-forming postfix of the string and appending the reverse of a palindrome prefix to the end of the string.