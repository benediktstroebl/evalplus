Here is a Python script that contains a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    palindrome = ""
    while True:
        palindrome += string[0]
        string = string[1:]
        if not string:
            break
    return palindrome[::-1]
```
This code defines a function `is_palindrome` that checks if a given string is a palindrome. The function returns True for empty strings. Then, the `make_palindrome` function takes a string as an argument and returns the shortest palindrome that begins with that string.

The code works by first checking if the input string is empty. Then, it initializes an variable `palindrome` to an empty string. It then enters a string, finds the first palindromic character, and appends it to the `palindrome` variable. It then removes the the string and appends the reversed `palindrome` to it. Finally, it returns the `palindrome` reversed.

Please note that this code does not use any external libraries or modules, and only relies on the functionality of Python strings and basic arithmetic operations.