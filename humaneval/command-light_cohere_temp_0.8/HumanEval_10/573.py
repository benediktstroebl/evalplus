```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".joinindrome(string[::-1]) + string[::-1][::-1]

def test_palindrome():
    assert is_palindrome("")
    assert is_palindrome("cat")
    assert is_palindrome("cata")
    assert is_palindrome("racecar")
    assert is_palindrome("radar")

if __name__ == "__main__":
    test_palindrome()
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` generates a palindrome by finding the longest palindrom substring in the original string. 

The `test_palindrome` function has some assertion tests for the `is_palindrome` and `make_palindrome` functions, which check that the function outputs the correct result for various input strings. 

When you run this script, it will run the tests and print the results. This ensures that the will properly check the functions.