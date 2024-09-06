Here is a Python script that contains a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    n = len(string)
    max_len = 0
    palindrome = ''
    for i in range(1, n):
        if is_palindrome(string[i:])):
            max_len = i
            palindrome = string[i:i] + palindrome

    # Append to the string reverse of a string prefix that comes before the palindromic suffix
    return palindrome + string[:max_len][::-1]
```
The script defines a function `is_palindrome` that checks if a given string is a palindrome, and another function `make_palindrome` that constructs the shortest palindrome using the `is_palindrome` helper function.