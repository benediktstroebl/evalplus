```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.joinimper(''.join(reversed(string[i:])) for i in range(1, len(string))
```

This function uses a simple algorithm to create the longest palindrome from the given string. It first checks if the time_palindrome(string) returns True, it returns the empty string. Otherwise, it finds the longest palindrome using the reversed string prefix and appends it to the original string.