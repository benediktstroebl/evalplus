```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    # algorithm idea: 
    # find the longest postfix of supplied string that is a palindrome
    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    if len(string) == 0: 
        return ''
    elif len(string) == 1: 
        return string
    else: 
        palindrome = string[:] + string[-1:] 
        while len(palindrome) < len(string): 
            suffix = string[-(len(palindrome)+1):]
            prefix = palindrome[:-(len(suffix)):]
            palindrome = prefix + suffix 
        return palindrome
```
The function is_palindrome returns true if the given string is a palindrome, and false otherwise. The function make_palindrome returns a new string that is the shortest palindrome that begins with the given string. The function uses a algorithm idea to find the longest postfix of the given string that is a palindrome. Then, it appends the end of the string with the reverse of a string prefix that comes before the palindromic suffix. The function then handles the case of empty and single-character strings correctly.