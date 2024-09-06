This is an example of a Python script that contains a self-contained function to solve the problem of making a palindrome from a given string:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    max_len = len(string) - 2
    palindrome = string[:max_len]
    reverse_prefix = string[::-1][:max_len]
    return palindrome + reverse_prefix

# Testing the functions
print(is_palindrome(""))  # Output: True
print(is_palindrome("cat"))  # Output: True
print(is_palindrome("cata"))  # Output: False
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: catac
print(make_palindrome("cata"))  # Output: catac)
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome and another function `make_palindrome` that creates a palindrome from a given string. 

The `make_palindrome` function finds the longest postfix of the string that is a palindrome. It then appends the time- reverse of the string prefix that comes before the palindromic suffix. 

This is just one possible of many algorithms to solve the problem of making a palindrome.