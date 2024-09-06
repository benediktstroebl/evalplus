A solution to the provided problem is a function that checks whether a given string is a palindrome. This function is below is self-contained and solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    
    return string +string[-2::-1] + string[:2]
```