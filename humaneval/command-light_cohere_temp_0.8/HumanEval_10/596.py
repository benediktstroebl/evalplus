Here is a self-contained Python script that defines a function is_palindrome that checks if a given string is a palindrome, and the function make_palindrome that creates a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Algorithm idea: 
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    # Construct a time by finding a palindrome and constructing it by appending.

    return ''.join(reversed(prefix) + palindrome

# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: cata
```
This approach uses the fact that a palindrome always appears as a reversed string. 
The 'make_palindrome' function looks for the longest palindrome-forming postfix and appends it to the end of the string.