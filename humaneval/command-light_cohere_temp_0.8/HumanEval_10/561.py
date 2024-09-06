```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string + string[::-1]
    return palindrome
```
The function 'is_palindrome' checks if a given string is a palindrome. The function 'make_palindrome' finds the shortest palindrome that begins with a supplied string.