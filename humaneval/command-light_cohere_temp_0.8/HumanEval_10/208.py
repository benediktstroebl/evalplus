```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ''
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:0:-1]  # [::-1] to get reverse of the prefix
    while len(palindrome) < len(string) and is_palindrome(string[len(palindrome)+1:]):
        palindrome += string[:len(palindrome)+1]
    
    return palindrome[::-1]
```
The code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function computes the shortest palindrome that begins with a given string. It uses a specific algorithm: it finds the longest palindromic prefix in the string, appends the rest of the string (excluding the palindrome itself), and reverses the entire string to get the desired result.