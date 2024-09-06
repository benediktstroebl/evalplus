Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".join([c for c in string if c != ' ' and is_palindrome(c)])[::-1]

def not_palindrome(string):
    return bool(is_palindrome(string))

# Test cases
print(make_palindrome(""))
print(make_palindrome("cat"))
print(make_palindrome("cata")))
print(make_palindrome("Ends it Fastly with us"))
print(make_palindrome("(email@en.com))"))
```

This script defines two functions, `is_palindrome` and `make_palindrome`, that solve the problem of checking if a given string is a palindrome, and then finding the shortest palindrom that begins with a supplied string, respectively. The functions are then tested using various test cases.