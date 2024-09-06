A solution using Python:
```Python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return string + make_palindrome(string[::-1])
```

This code defines two functions: `is_palindrome` checks if a given string is a palindrome or not. The `make_palindrome` function iteratively tries to construct a palindrome by appending the reverse of prefixes of the original string to the end of the string.