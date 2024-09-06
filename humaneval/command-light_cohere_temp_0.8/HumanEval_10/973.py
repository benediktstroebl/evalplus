Here's the solution:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest palindrome suffix of a string.
    suffix = max(string, key=len)
    
    # Extract the longest palindrome suffix
    reverse_suffix = suffix[::-1]

    # Construct the palindrome by appending the reverse_suffix
    return string + reverse_suffix
```
The function is_palindrome checks if a given string is a palindrome, and the function make_palindrome finds the shortest palindrome that begins with a supplied string.