```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    palindrome = ''
    for char in string:
        if char == palindrome[-1]:
            palindrome += char
        else:
            palindrome = char + palindrome[::-1]

    return palindrome
 ``` 
This script defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` creates a palindrome given a prefix. 
The `make_palindrome` function uses a simple algorithm to find the shortest palindrome that begins with the given prefix.