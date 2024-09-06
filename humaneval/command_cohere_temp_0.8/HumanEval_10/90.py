Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string+string[0:]

    # Find the shortest non-palindromic prefix.
    j = string.find(string[i:i+2], 1)
    if j == -1:
        return string[i:] + string[0:i][::-1]
    return string[i:] + string[0:j][::-1]
```

This code defines two functions: one to check whether a given string is a palindrome and one to construct the shortest palindrome starting with a supplied string. These functions are self-contained in that they only rely on standard Python libraries and do not require any external modules to function. 

The `make_palindrome` function efficiently determines the shortest palindrome by capitalizing on the knowledge that the longest palindromic suffix of a string always precedes the shortest non-palindromic prefix in the string. This allows us to reverse the prefix and append it to the string to create a palindrome without unnecessarily lengthening the string.