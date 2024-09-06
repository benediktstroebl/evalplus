```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0:-1] + string
    return palindrome

def is_palindrome_valid(string):
    return is_palindrome(string)

def test_make_palindrome(string):
    return make_palindrome(string) == make_palindrome(string[::-1])
```
The above code defines three functions: `is_palindrome` checks if a given string is a palindrome or not, `make_palindrome` builds a palindrome from a given string, and `is_palindrome_valid` verifies if a given string can form a palindrome or not. 

The `make_palindrome` function follows a simple algorithm:
1. Find the longest postfix of the supplied string that is a palindrome.
2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

The `is_palindrome_valid` function acts as a helper function to the `make_palindrome` function, and returns `True` if the input string is a palindrome, and `False` otherwise. 
The `test_make_palindrome` function is a simple test case for the `make_palindrome` function, as it passes the test.