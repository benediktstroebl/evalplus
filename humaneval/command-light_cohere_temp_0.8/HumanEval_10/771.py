```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1] 
    else:
        return 'Could not make a palindrome...'
``` 
This function, when given a string, checks if it is a palindrome. If the function determines that the string is a palindrome, it returns the string; otherwise, it returns the error message 'Could not make a palindrome...'.