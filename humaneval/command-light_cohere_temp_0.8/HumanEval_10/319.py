```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: return ''
    else:
        # Find the longest postfix of supplied string that is a palindrome
        palindrome = string
        while palindrome[::-1] != string[::-1]:
            palindrome = palindrome[1:] + palindrome[:-1]
        return palindrome
```
The code provides two functions:
- The `is_palindrome` function checks if a given string is a palindrome.
- The `make_palindrome` function finds the shortest palindrome that begins with a given string.

The algorithm idea is to find the longest postfix of the given string that is also a palindrome and construct a palindrome by appending the palindromic part and the reverse of a string prefix that comes before the palindrome.