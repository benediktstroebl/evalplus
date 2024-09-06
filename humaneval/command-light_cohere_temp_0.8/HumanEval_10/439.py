Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    # Find the longest postfix of supplied string that is a palindrome
    len_palindrome = len(string) - 1
    while True:
        if string[0::len_palindrome] == string[-1:]:
            break
        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        string = string[:-1] + string[-1:]
    return string
```

This script provides a function `make_palindrome` that finds the shortest palindrome that starts with a given string. The function uses a string slicing and concatenation to build the palindrome.