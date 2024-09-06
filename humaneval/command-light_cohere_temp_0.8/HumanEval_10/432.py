Here is a Python script that contains a self-contained function to solve the problem of making a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome_start = 0
    while True:
        if string[palindrome_start:].isupper():
            break
        palindrome_start += 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    reversed_palindrome = string[::-1][::-1][palindrome_start:]
    return string[:palindrome_start] + reversed_palindrome
```
The function is_palindrome checks if a given string is a palindrome. The function make_palindrome uses a simple algorithm to find the shortest palindrome that begins with the given string.