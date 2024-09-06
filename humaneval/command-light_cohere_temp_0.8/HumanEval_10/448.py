A Python function that addresses the problem of making a palindrome is shown below:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.joinindrome(string[::-1]) + string[-1:]

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))

# Run the function to test its output.
```