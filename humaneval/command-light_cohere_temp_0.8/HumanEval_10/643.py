```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return ""
    else:
        return "".joinend(string[:-1], string[::-1] + string[-1:])
```
The function is_palindrome checks if a given string is a palindrome. The function make_palindrome creates a palindrome using the idea of concatenating a prefix with the reversed suffix of the input string.