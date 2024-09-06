```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    Palindrome = [str.[::-1]
    prefix = string[:-1]
    return prefix + Palindrome
```
This code defines a Python function `is_palindrome` that checks if a given string is a palindrome. It returns `True` if the Palindrome. Then, the function `make_palindrome` is defined. This function aims to create the shortest palindrome of a given string.

The `make_palindrome` function takes a string `string` as input. It creates a string's reverse by using slicing operator (`[::-1]`). Then, it stores the prefix of the original string in a new variable `prefix`. It concatenates the `prefix` and the `Palindrome` to get the desired output.