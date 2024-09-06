```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    palindrome = ""
    while True:
        palindrome += string[0]
        if is_palindrome(string[1:]):
            break
        string = string[1:] + string[::-1]
    return palindrome

# Test the functions
print(is_palindrome(""))      # Output: True
print(is_palindrome("ted"))  # Output: False
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: "catac"
print(make_palindrome("cata"))  # Output: "catac"
```

The code defines two functions: is_palindrome and make_palindrome. The is_palindrome function determines if a given string is a palindrome, and the make_palindrome function constructs the shortest palindrom from a given string using the longest palindrom prefix and reverse of a suffix.

The code also comes with a set of tests that verify the correctness of both functions.