Here is a self-contained Python function that solves the problem of creating a palindrome from a given string:
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
        index = 1
        while index < len(string):
            if string[index] == palindrome[-1]: 
                index += 1 
            else: 
                break
        else: 
            break
        string = string[1:] + palindrome
    return palindrome
```
The `is_palindrome` checks if the given string is a palindrome or not, and the `make_palindrome` function uses a simple loop and character selection logic to construct the palindrome from the given string.