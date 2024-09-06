```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'Error: string is not a palindrome'

    palindrome_str = []
    while True:
        palindrome_str.append(char(string.lower() &next char that matches str.isprint(True)):
            return 'Error: string is empty'
        if char == ' ':
            return ''.reverse(palindrome_str)
        char = string[0]
        string = string[1:]
    return ''.reverse(palindrome_str)
```
The function `make_palindrome` uses the `is_palindrome` helper function to check if the string is already a palindrome. It then iterates over the generate a palindrome by appending the first character of the string to the reverse of the last characters in the string.

This is a self-contained function that can be used to solve the problem of making a palindrome in a given string.