```python
def is_palindrome(string): 
    """ Check if a string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Create a palindrome from a given string """
    if not string: return ""
    result = ""
    while True:
        Palindrome = string[::-1]
        if Palind == string[:-1]:
            result += string[1:] + Palind
            break
        else:
            result += Palind
    return result
```