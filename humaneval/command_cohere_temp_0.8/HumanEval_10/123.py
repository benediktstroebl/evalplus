Here's a Python script with a self-contained function that solves the problem using Python 3.10's `str.replace` method:
```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(reversed(string)))

    # If no palindromic suffix, simply return the string
    if i == -1:
        return string

    return string.replace(string[i:], '', 1)
```

This solution utilizes the recently introduced `str.replace` method in Python 3.10. Using this method, the longest palindromic suffix is found and then removed from the original string using a replacement of an empty string. This efficiently creates the desired palindrome.