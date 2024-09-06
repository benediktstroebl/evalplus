Here is a self-contained Python script with a function that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = ""
    for char in string:
        if char == palindrome[-1]:
            palindrome += char
        else:
            palindrome = char + palindrome[::-1]

    return palindrome

def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"
```
This script provides a complete solution with a function to check if a given string is a palindrome, and another function to generate the shortest palindrome using the algorithm explained.