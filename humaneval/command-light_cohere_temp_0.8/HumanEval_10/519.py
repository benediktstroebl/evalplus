```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """ 
    if not string:
        return ""
    
    #Longest palindrome of empty string
    if len(string) == 1: 
        return string
    
    #Longest palindrome of a single letter
    elif len(string) == 2: 
        return string
    
    #Find the longest palindrome of the string that follows the pattern
    #   ... [a-zA-Z]+ ...
    else: 
        #Find the longest palindrome with the reverse of the prefix 
        prefix = string[0:-1]
        palindrome = prefix + prefix[::-1]
        return palindrome
```