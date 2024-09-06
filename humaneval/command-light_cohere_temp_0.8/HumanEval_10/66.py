This function solve the problem of finding a palindrome of a given string using the fewest characters. 

```python
def is_palindrome(string):
    """ 
    Checks if the string is a palindrome or not 
    Returns: bool 
    """
    return string == string[::-1]

def make_palindrome(string):
    """ 
    Find the shortest palindrome that begins with a 
    supplied string. 
    Returns: string that is a palindrome.
    """
    longest palindrome = ""
    for char in string:
        if is_palindrome(char):
            longest_palindrome += char
    return longest_palindrome
```