Below is a Python code with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        # Find the longest palindrome using any prefix
        palindrome = find_palindrome(string[:1]) + string[1:][::-1]
        return palindrome

def find_palindrome(string):
    if not_palindrome(string):
        raise ValueError("Given string is not a palindrome.")
    else:
        return string
```
The code defines a function `find_palindrome` which returns the longest palindrome using any prefix of the string. The function also tests if the is a palindrome.