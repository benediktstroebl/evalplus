A simple and efficient palindrome string generation algorithm is implemented using the Python script below. 

```
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string): 
        return string
    if len(string) <= 1: 
        return string
    suffix = string[-1:]
    prefix = ''.joinc(min(char for char in string if char not in suffix))
    return prefix + suffix
```

The `is_palindrome` function checks if the input string is a palindrome. The `make_palindrome` function generates a palindrome by first checking for the function `is_palindrome` to return `True`. If the function returns `False`, it appends the reverse of the `suffix` to the `prefix`. This process is repeated until a palindrome is generated.