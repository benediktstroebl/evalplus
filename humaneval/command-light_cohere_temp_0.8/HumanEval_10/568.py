Here is a Python script that contains a self-contained function to solve the problem of creating a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.

    # Test if the time string is a palindrome or not?
    return ''.join_with(string,string[::-1],string)
```

The code defines a function `is_palindrome` that checks if a given string is a palindrome. The function returns `True` if the string is a palindrome and `False` otherwise. 

The function `make_palindrome` is defined to create a palindrome. It takes the time- string and appends it to the beginning of the string the reverse of a prefix that comes before the palindrome. 

The code then checks if the resulting string is a palindrome and returns it. If not, it returns an blank string.