```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """ 
    if not string:
        return ""
    palindrome = string
    reverse_prefix = string[::-1]
    while True:
        if reverse_prefix == palindrome:
            break
        palindrome = palindrome + reverse_prefix
        reverse_prefix = string[::-1]
    return palindrome
```
This code defines two functions, is_palindrome and make_palindrome, which are used to check if a given string is a palindrome and to generate a palindrom from a given string, respectively.

These functions are self-contained and do not rely on any other functions or modules, which means they can be easily included into any other project or code base.