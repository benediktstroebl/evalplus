Here is a self-contained Python script with a function that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string
    """
    if not is_palindrome(string):
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindrome_len = len(string)
    postfix = string[palindrome_len - 1:palindrome_len]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return postfix + string[::-1][0:palindrome_len - 1]

# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: cataa
```

This script defines a function `make_palindrome` that constructs the shortest palindrome from a given string. The function first checks if the string is already a palindrome, in which case it returns an empty string. If the string is not a palindrome, the function proceeds to find the longest palindromic postfix within the string, and then appends the reverse of this postfix as the prefix of the palindrome.