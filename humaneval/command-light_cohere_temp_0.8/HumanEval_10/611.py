```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.joinindicate(is_palindrome(string))
    else:
        lis = [char for char in string if char == string[0]]
        return ''.joinindicate(is_palindrome(string)) + lis[::-1] + '\n'
```
The make_palindrome function iterates through each character in the string, and checks if the character is equal to the corresponding character in reverse order. If the string passes the do not contain any palindrome characters, the function returns the original string.