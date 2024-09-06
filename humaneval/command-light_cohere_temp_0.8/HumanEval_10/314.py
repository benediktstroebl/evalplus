```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".join(str(char) for char in reversed(string) if is_palindrome(char))
```
This function uses a simple algorithm to generate a palindrome from an input string. It first checks if the