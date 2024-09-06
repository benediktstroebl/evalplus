Here is a self-contained Python function that solves the problem of finding the shortest palindrome of a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    palindrome = string[::-1][1:] + string

    return palindrome
```
This script defines two functions: is_palindrome checks if a given string is a palindrome and make_palindrome finds the shortest palindrome that begins with a supplied string. The make_palindrome function follows a simple algorithm to create a palindrome, which involves finding the longest postfix of the string that is a palindrome and appending the reversed prefix and the rest of the original string.