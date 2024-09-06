```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` builds a palindrome from a given string. The `not_palindrome` function checks if the input string can be a palindrome or not, and then calls the `make_palindrome` function to create a palindrome. The last_palindrome function is then used to check if the output of `make_palindrome` is a palindrome or not.