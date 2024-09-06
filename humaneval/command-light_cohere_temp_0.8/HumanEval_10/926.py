Here is a Python script with a self-contained function that solves the problem of making a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    length = len(string)
    reversed_string = string[::-1]
    for i in range(1, length):
        if is_palindrome(string[:i] + reversed_string + string[i:]):
            return string[:i] + reversed_string + string[i:]
    return string
```
The code provides a function is_palindrome that checks if a given string is a palindrome, and another function make_palindrome that finds the shortest palindrome.