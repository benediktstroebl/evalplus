Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    """ Check if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Create a palindrome from a non-palindrome string """
    
    if not_palindrome(string):
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:string.find(string[::-1], len(string))] + string[::-1] 
    return palindrome

# Driver code
print(make_palindrome('cata'))
print(make_palindrome(''.join'))
print(make_palindrome('cat'))
print(make_palindrome('coda'))
print(make_palindrome('catt'))
print(make_palindrome(''.cmx'))

def not_palindrome(string):
    if not string: 
        return False
    return is_palindrome(string)
```