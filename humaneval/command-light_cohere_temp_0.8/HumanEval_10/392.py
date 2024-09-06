```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0] + string[::-1]
    return palindrome
```
This function checks if a given string is a palindrome. It returns True if the Palindrome condition is satisfied, and False otherwise.