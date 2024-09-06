```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''.join(x if is_palindrome(x) else x[::-1] for x in string)
    return string
```
The code is a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome, and then creates the palindrome.  using the  a simple algorithm that uses the supplied string and creates the longest palindrome using a prefix and postfix technique.