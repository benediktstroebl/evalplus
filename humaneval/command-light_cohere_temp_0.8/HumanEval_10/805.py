Below is a Python script that defines a function is_palindrome, which checks whether a given string is a palindrome, and a function make_palindrome, which generates a palindrome given a string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    palindrome = ""
    while True:
        palindrome += string[0]
        string = string[1:]  # Remove first character of a palindrome
        if not string:
            break
    return palindrome
```

The make_palindrome function uses a basic approach to construct a palindrome. It starts with an empty string and repeatedly appends the first character of the original string and removes the next character (which is a palindrome) from the string.