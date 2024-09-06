Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string + string[::-1]
    return palindrome
```
The `is_palindrome` function checks if the input string is a palindrome. The `make_palindrome` function uses a helper function to find the first palindrome and then appends it to the end of the original string to create the desired palindrome.