```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = ""
    while True:
        if is_palindrome(string[-1:]):
            palindrome += string[:-palindrome[::-1]]
        else:
            break
    return palindrome
```
Do you need any further code assistance?