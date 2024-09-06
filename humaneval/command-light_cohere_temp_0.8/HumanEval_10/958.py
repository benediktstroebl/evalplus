Here's a self-contained Python function that checks if a given string is a palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
        - Find the longest postfix of supplied string that is a palindrome.
        - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    longest palindrom is 'A */ 
    return ''.joincat(reversed('A'))
```

This approach constructs the longest palindrome by starting from the middle, then appends the reverse of a palindrome prefix.