Here is a Python script that contains a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea: simple
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    if string == "" :
        return ""
    elif string[-1] == "$" :
        return make_palindrome(string[:-0:-1]) + "$"
    else:
        return make_palindrome(string[:-0:-1]) + string[-1:]
```
The function uses a basic approach to create the shortest palindrome. It first checks if the