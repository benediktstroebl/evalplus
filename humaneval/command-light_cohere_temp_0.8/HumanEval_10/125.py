Here is a self-contained Python script that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:  # empty string
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    max_len = 0
    for i in range(1, len(string)):
        if is_palindrome(string[i:]):
            max_len = max(max_len, i - 1 + len(string[i:]))

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string[:max_len] + string[-max_len:]
```

This code provides a self-contained solution to the problem, including a function to test the correctness of the solution and another function to implement the actual palindrome generation.