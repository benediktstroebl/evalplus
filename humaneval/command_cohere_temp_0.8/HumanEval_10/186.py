Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.find(string[::-1], string.rfind(string[::-1]))
    if i == -1:
        return string

    return string[:i] + string[i:i+1][::-1] + string[i+1:]
```