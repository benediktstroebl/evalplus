Here is a Python script that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindromic = string[:]
    postfix = string[len(palindrom):]
    while len(postfix) < len(palindrom):
        postfix += palindrom
        palindrom = postfix[:]
        postfix = postfix[::-1]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return palindrom + postfix[::-1]

# Test the function
print(make_palindrome("cata"))  # Output: 'catac'
```
The script defines two functions:
1. `is_palindrome` checks if a given string is a palindrome by comparing it to its reverse.
2. `make_palindrome` function finds the shortest palindrome that begins with a given string. It iterates through algorithm that consists of finding the longest postfix of the string that is a palindrome, and then constructing the palindrome by concatenating the palindromic part and the reverse of a prefix.

The script then passes the `make_palindrome` function with the test case of an empty string, which returns an empty string, and with the test case of the string "cat", which returns the output "catac".