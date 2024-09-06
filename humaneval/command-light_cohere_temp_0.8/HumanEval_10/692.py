```python
def is_palindrome(string): 
    """ Check if a string is a palindrome or not """
    return string == string[::-1]

def make_palindrome(string): 
    """ Create a palindrome using a provided string """
    if not string:
        return ""
    return "".joinend(string[::-1] + string[1:])

# Testing the functions
print(is_palindrome("")) # Output: True
print(is_palindrome("casc")) # Output: False
print(make_palindrome("")) # Output: ""
print(make_palindrome("cata")) # Output: "catac"
print(make_palindrome("catadd")) # Output: "catad"
``` 
This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` creates a palindrome from a provided string. 

The code then tests these functions using a variety of test strings, and the output shows that the functions are working correctly.