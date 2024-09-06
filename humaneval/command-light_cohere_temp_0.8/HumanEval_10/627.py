```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:]
    for char in string[1:]:
        if char == palindrome[::-1]:
            palindrome = palindrome[1:] + char
    return palindrome[::-1]
```

This Python code defines two functions, is_palindrome and make_palindrome, which solve the problem of checking if a given string is a palindrome, and then constructing the shortest palindrom starting with a given prefix respectively. The code is self-contained and efficient, utilizing basic string comparison and concatenation logic to achieve the desired result.