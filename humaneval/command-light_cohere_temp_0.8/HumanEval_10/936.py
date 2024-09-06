```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:  # empty string
        return ""
    else:
        # Find the longest postfix of supplied string that is a palindrome
        lst = [c for c in string if c.isalpha()]
        previous = ''
        for c in lst:
            if c.isalpha():
                # previous = c
        else:
            break
        return string[:previous] + string[-previous:]
```
The above code defines a set of functions that take a string, and return a palindrome of the original string, or an empty string if the original is empty.