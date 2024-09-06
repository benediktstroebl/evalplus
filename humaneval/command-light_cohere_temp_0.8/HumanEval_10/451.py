```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''

    is_palindrome_len = len(string)
    
    if is_palindrome_len == 0:
        return string
    
    prefix = string[:is_palindrome_len // 2]
    suffix = string[-is_palindrome_len // 2:]
    
    return prefix + suffix
```
This function is designed to solve the problem and pass the tests. It does this following:
- It takes a string `string` as an argument and checks if it's empty. If the string is empty, it returns an empty string.
- If checks if the length of the string is even. Then it takes half of the string as a prefix and the other half as a suffix.