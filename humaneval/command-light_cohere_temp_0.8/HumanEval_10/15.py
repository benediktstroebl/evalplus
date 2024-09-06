A solution using Python:
```Python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return ' palindrome not possible'
```
The code defines a function `make_palindrome` that checks if a given string is a palindrome, and if so, constructs and returns a new string that is a palindrome. The function `is_palindrome` checks if the string is a palindrome by using the slicing operator `::-1` to reverse the string and compare it with the original string. 

The code also defines a helper function `is_palindrome` that returns `True` if the string is a palindrome, and `False` otherwise.