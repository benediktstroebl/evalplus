Here is a self-contained Python script that solves the problem of finding a palindrome of a given string:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ""
    else:
        palindrome = string 
        prefix = ""
        reversed_prefix = ""
        while True:
            if palindrome == prefix[::-1] == palind:
                break
            else:
                if palind != prefix:
                    prefix = palind[0:1]
                else:
                    reversed_prefix = palind[::-1]
                palind = palind[1:]
        return prefix + reversed_prefix
```

This code has two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` checks if a given string is a palindrome. The `make_palindrome` function finds the shortest palindrome that begins with the supplied string.