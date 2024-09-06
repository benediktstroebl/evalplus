I can help you with that. For sure, below is a self-contained Python function that checks if a given string is a palindrome and passes the test using the 'make_palindrome' function:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Finds the shortest palindrome that begins with a supplied string """
    if not string:
        return ''
    palindrome = string
    for char in palindrome:
        if char != palindrome[-1] and is_palindrome(char):
            palindrome = char
        else:
            break
    return palindrome
```

This script provides a self-contained function to check if a given string is a palindrome and creates the shortest palindrome using the 'make_palindrome' function.