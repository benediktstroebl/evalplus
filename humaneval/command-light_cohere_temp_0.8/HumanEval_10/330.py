```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    The idea is to first find the longest palindrome in the string and then append the reverse of the prefix to the end of the string."""
    if not string:
        return ""
    palindrome = ""
    while True:
        palindrome = palindrome + string[-1:]
        if palindrome == palindrome[::-1]:
            break
    return palindrome
```