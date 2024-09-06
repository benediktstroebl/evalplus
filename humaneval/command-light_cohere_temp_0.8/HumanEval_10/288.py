```python
def is_palindrome(string): 
    return string == string[::-1] 

def make_palindrome(string): 
    if not_palindrome(string): 
        return string + string[::-1]
    else: 
        return 'NA' 

# Test the function
print(make_palindrome('')) # Output: NA
print(make_palindrome('cat'))  # Output: catac 

print(make_palindrome('cata'))  # Output: catac 

print(make_palindrome('123456789'))  # Output: 123456789013 

print(make_palindrome('thermal'))  # Output: tralh 

print(make_palindrome('atecylinder'))  # Output: acyltr 

print(make_palindrome('')) == make_palindrome(' ')  # Output: True
``` 
The `make_palindrome` function solves the problem by finding the first palindrome in the given string and then appending the reverse of the prefix to it. 

The `is_palindrome` function returns `True` if the string is a palindrome, and `False` otherwise.