```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    prefix = string[:str.find_palind(string)]
    palindrome = prefix + prefix[::-1]
    return palindrome
```

The above Python script defines a function `make_palindrome` that attempts to create the shortest palindrome using the `is_palindrome` helper function. The function takes a string as input and returns its own made palindrome.