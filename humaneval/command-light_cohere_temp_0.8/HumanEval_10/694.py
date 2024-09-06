Below is a Python script with a self-contained function that solves the problem of creating a palindrome using the provided algorithm:

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ""
    
    # Find the longest palindrome prefix
    palindrome = string
    
    while True:
        prefix = palindrome[: len(palindrome) - 1]
        if is_palindrome(prefix):
            palindrome = prefix + palindrome[::-1]
            break
    
    return palindrome
```

The function is_palindrome checks if the given string is a palindrome. The function make_palindrome computes the shortest palindrome that begins with the input string. The algorithm works by first trying to find the longest palindrome prefix and then appends the reverse of the string prefix that comes before the palindromic suffix.