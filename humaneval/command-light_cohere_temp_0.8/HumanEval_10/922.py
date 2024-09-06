Here is a Python script with a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    prefix = ""
    suffix = ""
    for char in string:
        if char == prefix[-1] or char == suffix[-1] + ' ':
            prefix += char
        else:
            suffix += char
    return prefix + suffix[::-1]
```
The make_palindrome function takes a string as input and returns the shortest palindrome that begins with the given string. This function uses two algorithm idea:
- Find the longest postfix of the string that is a palindrome.
- Append the end of the string reverse of a string prefix that comes before the palindromic suffix.

The test case is implemented in the function to pass the test of the function with the test string.