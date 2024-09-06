```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join
        postfix = ''
        for char in string:
            if char == postfix[-1] and is_palindrome(postfix):
                postfix += char
                else:
                postfix = char
        return postfix + postfix[::-1]

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))
```
The function `make_palindrome` is a recursive function that uses a helper function `is_palindrome` to check if a given string is a palindrome. It then iterates through string and finds the longest postfix of a palindrome and appends it to the `postfix` variable. Finally, it reverses the the palindrome and returns the string.