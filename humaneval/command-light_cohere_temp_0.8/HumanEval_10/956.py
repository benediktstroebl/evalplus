I have provided a self-contained Python function that solves the problem of finding the shortest palindrome using the algorithm provided:

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    palindrome = ""
    while True:
        palindrome = palindrome + string[::-1] + string
        if is_palindrome(palindrome):
            break
    return palindrome
```

This function uses a while loop to append the reverse of the current string prefix to itself until it becomes a palindrome. It is then returns the time.