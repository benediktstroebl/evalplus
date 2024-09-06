```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Find the longest palindrome substring 
    # in the original string that is also a palindrome
    palindrome = ""
    for char in string:
        if char == palindrome[-1] and palindrome not == "" :
            palindrome += char
        else 
            palindrome = char

    # Reverse the prefix and append the palindrome 
    return string[:len(palindrome)] + palindrome[::-1]
```

The code defines two functions, `is_palindrome` and `make_palindrome`, to determine if a given string is a palindrome and to construct a palindrome from a given string. The code is self-contained and uses only these two functions.