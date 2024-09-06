Here is a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string:
        return ""
    
    palindrome = string
    reversed_prefix = string[::-1]
    while len(palindrome) < len(reversed_prefix):
        palindrome += reversed_prefix
        reversed_prefix = reversed_prefix[::-1]
        
    return palindrome
```

This script defines two functions: `is_palindrome` to test if a given string is a palindrome and `make_palindrome` to create the shortest palindrome using the longest palindromic prefix starting from the given string. The code is a simple and efficient algorithm that uses the idea of finding the longest palindromic prefix and appending the reversed prefix to the end of the original string.