```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    palindrome = ""
    while True:
        palindrome += string[0]
        n = 1
        while n < len(string) and string[n] == palindrome[-1] + string[n]:
            n += 1
        if n == len(string):
            return palindrome
```