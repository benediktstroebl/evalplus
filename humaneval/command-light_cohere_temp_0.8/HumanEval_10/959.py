```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[1:])

def not_palindrome(string):
    return is_palindrome(string) and make_palindrome(string) == string
```
The `make_palindrome` function follows a simple algorithm: 
 - It finds the longest postfix of the string that is a palindrome. 
 - Then then appends the string reversed of a string prefix that comes before the palindromic suffix. 

The `is_palindrome` function simply returns true if the string is the same when reversed.