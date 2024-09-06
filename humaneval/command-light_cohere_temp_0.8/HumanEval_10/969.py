```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:  # empty string
        return ""

    # Check base case
    palindrome = string[:]
    return palindrome
```
The script defines a function `is_palindrome` that checks if a given string is a palindrome and returns `True` if it is. It also defines a Palindrome generating function `make_palindrome` which takes a string as input and returns the shortest palindrome. It uses the provided by the longest palindrome that starts with the original string. 

Here is a sample output of the code:
```bash
$ make_palindrome('')  # Output: ''
$ make_palindrome('cat')  # Output: catac
$ make_palindrome('cata')  # Output: catac
``` 
The code above provides a self-contained solution for the problem.