```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])

def not_palindrome(string):
    return make_palindrome(string) == string

# tests
print(is_palindrome(""))   # True
print(is_palindrome("t"))   # True
print(is_palindrome("R"))   # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello")))  # False
print(is_palindrome(" programming is fun ))  # False
print(make_palindrome(""))   # ""
print(make_palindrome("cat"))   # "catac"
print(make_palindrome("cata"))   # "catac"
print(make_palindrome("elephant")))  # "hfelephantpntt"
```
The function `make_palindrome` takes a string `string` as input and recursively finds the shortest palindrome that starts with the string. The function then checks if the string is already a palindrome and returns it, else it appends the reverse of the palindrome prefix to the string.

The function uses a recursive approach to find the palindrome. The time complexity of this function is O(n), where n is the length of the input string.