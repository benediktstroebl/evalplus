```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    suffix = string[-1:]
    prefix = string[:0:-1]
    return prefix + suffix.
```

The make_palindrome function generates the shortest palindrome using the is_palindrome function. This works by finding the longest postfix of the string that is a palindrome, and then appending the reverse of a string prefix that comes before the palindromic suffix.