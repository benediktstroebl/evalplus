Here's a Python script with a self-contained function that solves the problem of forming the shortest palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    # Reverse the non-palindromic prefix and concatenate
    return make_palindrome(string[:j]) + string[j:i][::-1] + make_palindrome(string[i+1:])
```

This code defines a function `make_palindrome` that takes a string as an input and tries to find the shortest palindrome that starts with the given string. The solution uses two main steps:
1. Find the longest palindromic suffix of the given string.
2. Find the longest non-palindromic prefix before the palindromic suffix.

Then the code reverses the non-palindromic prefix and concatenates it with the original supplied string to achieve the shortest palindrome possible. The base case handles when the input string is empty, and the function returns the empty string. 

The function is_palindrome checks whether a given string is a palindrome by comparing it to its reverse.