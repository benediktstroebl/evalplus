```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    string = string.split(" ",",)[::-1]
    return "".join(char for char in string if char in 'cotcin')
```