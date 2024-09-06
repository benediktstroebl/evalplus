```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea: 
    # - Find the longest postfix of supplied string that is a palindrome.
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string:
        return ""
    
    palindrome = ""
    for char in string:
        if char == palindrome[-1] and palindrome:
            palindrome += char
        else:
            palindrome = char + palindrome
            if len(palindrome) > len(string) // 2:
                break

    return palindrome[::-1]
```
This Python code defines a function `make_palindrome` that constructs the shortest palindrome using a character-building strategy. The `is_palindrome` function tests whether a given string is a palindrome.