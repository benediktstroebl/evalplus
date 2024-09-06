```python
def is_palindrome(string: str) -> bool:
    """ Check if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Create a palindrome from a non palindrome string """
    
    # Algorithm idea: 
    # - Find the longest postfix of supplied string that is a palindrome.
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string:
        return ""

    # Remove all non-alphindrome characters and keep the length
    palindrome_start = len(string) - 1
    string = string[::-1][::-1][palindrome_start:][::-1]
    return string
```