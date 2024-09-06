```python
def is_palindrome(string): 
    return string == string[::-1]
    
def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea: 
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = ''
    postfix = ''
    for char in string:
        if char == postfix[-1] and postfix != '':
            palindrome += char
            postfix = ''
        else:
            postfix += char

    return palindrome + postfix[::-1]
```

The above script defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome of the string. This function uses a first checks with `is_palindrome` function to see if the input string is already a palindrome, and if so, it returns the original string. If the input is not a palindrome, the function uses a simple algorithm to find the longest postfix of the string that is also a palindrome, and then appends the reverse of this postfix prefix to the original string. 

Please note that this implementation is not the most space-efficient, but it serves as a good starting point for understanding the problem.