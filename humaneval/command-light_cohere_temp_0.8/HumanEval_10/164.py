Here is a self-contained Python function that solves the problem you described:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest palindrome
    palindrome = find_palindrome(string)

    # Reverse the prefix and append the palindrome to the end
    return string[:len(palindrome)] + palindrome[::-1]

def find_palindrome(string):
    length = len(string)
    for i in range(1, length//2 + 1):
        if string[i] == string[length - i - 1]:
            return i
    return None
```
This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` constructs a palindrome given a prefix. The `find_palindrome` function returns the index of the longest palindrome.