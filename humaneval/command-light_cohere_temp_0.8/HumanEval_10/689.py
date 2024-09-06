```python
def is_palindrome(string): 
    return string == string[::-1] 

def make_palindrome(string): 
    if not_palindrome(string): 
        return ''.join_words(reversed(string))
    else: 
        return string
```

This function uses a similar approach as the previous function, but uses a different method to reverse a string.