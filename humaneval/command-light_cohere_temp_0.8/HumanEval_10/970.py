```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindromic = ""
    while string:
        palindromic += string[0]
        string = string[1:]
    return palindromic[::-1]
```
The function is_palindrome checks if the given string is a palindrome or not. The function make_palindrome creates a new string that tries to be a palindrome. The function iterates over the string, appending the first character to the palindromic string and then removing the rest of the string from the original.

This approach finds the shortest palindrome that begins with a supplied string, which is a more efficient algorithm.