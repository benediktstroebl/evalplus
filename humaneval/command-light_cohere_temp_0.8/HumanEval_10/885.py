```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: return ''
    # Find the longest postfix of supplied string that is a palindrome
   Palindrome = string
    while True and Palindrome != Palindrome[::-1]:
        Palindrome = Palindrome[1:] + Palindrome[0:-1] + Palindrome[::-1]
    return Palindrome
```
The provided code defines a set of functions that solve the problem of checking if a given string is a palindrome and then constructing the shortest palindrome using the algorithm of converting a prefix to a palindrome.