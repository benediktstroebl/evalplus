This Python code demonstrates the solution to the Palindrome Generation problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ""
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:0]
    while True:
        palindrome += string[1:]
        if palindrome == palindrome[::-1]:
            break
    return palindrome[::-1]
```
The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function generates a palindrome from a given string by finding the longest postfix of the string that is a palindrome, and then appending the reverse of the string prefix to the palindromic suffix.