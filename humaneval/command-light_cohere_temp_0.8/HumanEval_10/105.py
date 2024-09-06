Here's the Python code for the provided markdown code block:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:  # handle empty string
        return ""

    lis = list(string)
    lis.sort()  #palindrome_prefix = lis[0]

    for i in range(1, len(lis)):
        if lis[i] == lis[i - 1] + lis[i - 2]:  # found palindrome
            palindrome = lis[0] + lis[i:]
            break
    return palindrome
``` 
This code defines two functions, is_palindrome checks if a given string is a palindrome, and make_palindrome creates a palindrome for the given string.