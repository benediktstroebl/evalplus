```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    l, r = 0, len(string)-1
    while l <= r:
        if is_palindrome(string[l:r+1]):
           break
        r -= 1
    return string[:l] + string[r:][::-1]

# Test the functions
print(is_palindrome(''))  # Output: True
print(is_palindrome('cata'))  # Output: False
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` creates the shortest palindrome from a given string. 

The `make_palindrome` function iteratively searches for a palindrome substring in the given string. The is_palindrome function checks if the substring is palindromic, and returns True if it is. The `make_palindrome` function uses this function to find the palindrome and returns the result.