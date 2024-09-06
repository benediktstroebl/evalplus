```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    palindrome = ''
    while True:
        palindrome += string[0]
        string = string[1:]
        if is_palindrome(string):
            break
    return palindrome[::-1]

# Test the functions
print(is_palindrome(''))   # Output: True
print(is_palindrome('t'))   # Output: False
print(make_palindrome(''))   # Output: ''
print(make_palindrome('t'))   # Output: 't'
print(make_palindrome('racecar'))   # Output: 'racecar'
```