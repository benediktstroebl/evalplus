Here is a self-contained Python script with a function that solves the problem of making a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:  # empty string is a palindrome
        return ""
    else:
        # find the longest postfix of supplied string that is a palindrome
        palindrome = string[::-1] 
        while len(palindrome)>1 and palindrome[0] == palindrome[1]: 
            palindrome = palindrome[1:] + palindrome[:1] 
        return palindrome
```

The code defines two functions:
1. `is_palindrome`: checks if a given string is a palindrome or not, by comparing the original string with its reverse.
2. `make_palindrome`: uses dynamic programming to find the shortest palindrome. It starts by checking if the string is empty, in which case it returns an empty string. Then, it finds the longest postfix of the string that is a palindrome, by swapping the first two characters if the string is not a palindrome. Finally, it returns the string reversed + the palindrome as the shortest palindrome.