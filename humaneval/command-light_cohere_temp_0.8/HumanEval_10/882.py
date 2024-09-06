This script defines a function that checks if a given string is a palindrome, then creates the shortest one that starts with the given string.

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """
    if not string:  # empty string is always a palindrome
        return string
    
    if len(string) == 1:  # cannot make a palindrome with only one character
        return string
    
    # Find the longest postfix of supplied string that is a palindrome
    postfix = ''.join
    while True:
        palindrome = postfix + string[0]
        if is_palindrome(palindrome):
            postfix = string[1:]
            break
        else:
            break
    
    return postfix[::-1] + palindrome
```