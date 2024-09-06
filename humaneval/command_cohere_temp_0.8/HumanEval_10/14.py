Here's a Python script with a self-contained function that solves the problem of forming the shortest palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string
    
    return string[:i] + string[i:i][::-1] + string[i+1:]
```

The function `make_palindrome()` takes a string and returns the shortest palindrome that begins with the provided string. The method works by finding the longest palindromic suffix of the supplied string and then reversing a corresponding prefix to form the shortest palindrome.