Here is a self-contained Python script that solves the problem of making a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    if len(string) == 1:
        return string
    mid = string[: len(string) // 2]
    return (mid + mid[::-1]) + string[len(string) // 2:]
```
This script defines two functions: `is_palindrome` which checks if a given string is a palindrome or not, and `make_palindrome` which constructs a palindrome from a given string. The `make_palindrome` function uses a divide and conquer approach to find the shortest palindrome, it first checks if the given string is empty or has only one character, if so it returns the string. Then, it finds the longest palindromice prefix in the string and divides the string into two parts: one with the palindrome prefix and another with its reverse. Then, it concatenates these two parts together with the opposite end to reverse the whole string, forming a palindrome.