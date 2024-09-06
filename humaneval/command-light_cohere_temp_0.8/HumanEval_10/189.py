```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """ 
    if not string:
        return ''
    return make_palindrome(string[::-1]) + string 

# Testing the function
print(is_palindrome(""))  # True
print(is_palindrome(""))  # False
print(is_palindrome("hello"))  # True
print(is_palindrome("world"))  # False
print(make_palindrome("hello")))  # hollwa
print(make_palindrome(""))   )  # Returns the empty string
print(make_palindrome("world"))  # catac
```