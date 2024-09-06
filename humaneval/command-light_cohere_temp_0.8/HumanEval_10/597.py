Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    postfix = ''
    while True:
        if is_palindrome(postfix + string[::-1]):
            break
        postfix += string[:-1]

    return postfix[::-1]
```
The function `is_palindrome` checks if a given string is a palindrome. The function `make_palindrome` builds the shortest palindrome using the `is_palindrome` function. The function is not using any extra space and does not depend on the length of the input string.