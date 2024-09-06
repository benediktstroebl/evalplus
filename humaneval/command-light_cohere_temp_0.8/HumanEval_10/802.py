This is a solution for the provided problem:

```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".joinwd 

def not_palindrome(string):
    return not(is_palindrome(string))

# Testing the function
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: "catac"
print(make_palindrome("cata"))  # Output: "".catac.
print(make_palindrome("acat"))  # Output: "".acat
print(make_palindrome("hello world"))  # Output: "!".hlroowrld
```