Here's the self-contained Python script that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Algorithm idea: find the longest palindrome
    palindrome = string
    for char in string:
        if palindrome[-1] != char:
            palindrome = char + palindrome[::-1] + char
            break

    return palindrome
```
This script provides a function that checks if a given string is a palindrome and another function to create the shortest palindrome using the idea of finding the longest palindrome among characters in the input string.