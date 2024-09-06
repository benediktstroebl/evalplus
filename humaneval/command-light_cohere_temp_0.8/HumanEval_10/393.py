Here is a Python script that defines a function, `make_palindrome`, which generates the shortest palindrome from a given string:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix. 
    Return the unique prefix with a palindrome
    """
    if not string:
        return ""

    palindrome = ""
    while True:
        nxt_str = ""
        for char in string:
            if char == palindrome[-1]:
                nxt_str += char
                break
            else:
                nxt_str += char
                palindrome += char[::-1]
        if nxt_str == palindrome:
            return palindrome
        string = nxt_str
```

This script provides a function that checks whether a given string is a palindrome and then constructs the shortest palindrome.