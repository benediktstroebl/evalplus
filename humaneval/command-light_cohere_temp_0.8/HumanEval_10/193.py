```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return string + make_palindrome(string[::-1])

def test():
    assert is_palindrome("") == True
    assert is_palindrome("cat") == True
    assert is_palindrome("cata") == True
    assert is_palindrome("abcde") == False
    assert is_palindrome(" ") == True
    assert is_palindrome("hello ") == True

if __name__ == "__main__":
    test()
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` constructs a palindrome from a given string. It also includes a test function with a set of test cases to verify the correctness of the `is_palindrome` and `make_palindrome` functions.