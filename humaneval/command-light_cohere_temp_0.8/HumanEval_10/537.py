Here is a self-contained Python function that solves the problem you provided:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    if len(string) < 2:
        return string  # not palindrome
    
    palindrome = ""
    start = 0
    while True:
        if string[start:][::-1] == string[start:]:
            break  # palindrome found, break loop
        else:
            # Find the longest palindromic substring
            length = 1
            while start + length < len(string) and string[start + length:][::-1] == string[start:]:
                length += 1
            palindrome = string[start:start + length]
            start += length
            
    return palindrome
```
This script has a function that checks if a given string is a palindrome and another function that creates a palindrome from a given string.