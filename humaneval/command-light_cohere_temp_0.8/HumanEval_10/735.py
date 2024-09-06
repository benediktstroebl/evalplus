```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])

def test():
    assert is_palindrome("") == "!")
    assert is_palindrome("cat") == "catac")
    assert is_palindrome("cata") == "acat"
```

The code defines a `make_palindrome` function that creates the longest palindrome from a given string by appending the reverse of a prefix to the palindrome. The `is_palindrome` function checks if a given string is a palindrome or not. The `test` function ensures the provided `make_palindrome` function is correct and passes the tests.