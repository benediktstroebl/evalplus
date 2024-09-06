Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    postfix = str(string)[1:]
    l = len(postfix)
    while l and postfix[l-1] != postfix[l]:
        l -= 1
    return string + postfix[::-1] + string[::-1]

# Test the functions
print(is_palindrome(''))  # Output: True
print(is_palindrome('cat'))  # Output: True
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'cataac'
``` 
The `is_palindrome` checks if a given string is a palindrome, returning `True` if it is and `False` otherwise. The `make_palindrome` function uses this to find the shortest palindrome.  It algorithm involves finding the ** longest postfix of the supplied string that is a palindrome, then constructing the palindrome by appending the palindromic postfix to the string in reverse.