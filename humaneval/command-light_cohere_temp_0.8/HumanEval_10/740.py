Here is a self-contained Python function that solves the problem of checking if a string is a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    else:
        # Find the longest postfix of supplied string that is a palindrome
        pal = [char for char in string if char == string[1:]]
        if not pal:
            pal = [string[::-1]]
        else:
            pal = pal + [string[1:]]
        
        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        return palindrome = ''.join(pal) + string[::-1]
```
The function checks if the string is the same when reversed, and if it is, it is a palindrome. It then constructs a palindrome by finding the longest palindromic postfix and appending it to the reversed prefix.