Here is a Python script with a self-contained function that solves the problem of finding the longest palindromic substring in a given input string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    # Algorithm idea simple
   
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return ''.join[::-1] + string[1:]
```

The function works by first checking if the input string is a palindrome. If it is, the function returns False. Otherwise, it finds the longest palindrome substring of the input string, which is equal to the longest palindromic substring. The function then appends the end of the string reverse of a string prefix that comes before the palindromic suffix.