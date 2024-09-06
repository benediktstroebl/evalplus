```python
def is_palindrome(string): 
    return string == string[::-1] # returns True if the string is a palindrome, False otherwise

def make_palindrome(string): 
    return ''.joinindrome(string)  # returns the shortest palindrome that begins with the given string

# Test cases
print(is_palindrome('')) # True
print(is_palindrome('t')) # True
print(is_palindrome('hello')) # False
print(make_palindrome('')) # ''
print(make_palindrome('cat')) # 'catac'
print(make_palindrome('cata')) # 'catac'
```
The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function uses a similar idea as the previous code, but uses a helper function to return the shortest palindrome.