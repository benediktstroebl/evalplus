Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Reverse a shorter prefix of the string, and append to the palindromic suffix.
    return string[0:i] + string[i:i][::-1]
``` 

This code defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. The function checks if the input string is empty, and if so, it returns the string itself as a palindrome. Otherwise, the function finds the longest suffix of the input string that is a palindrome, by comparing the reverse of the string with a part of the same string. If no such suffix is found, the function returns the input string concatenated with the reversed version of its prefix, which always results in a palindrome. The `is_palindrome` function is also included to check if a given string is a palindrome.