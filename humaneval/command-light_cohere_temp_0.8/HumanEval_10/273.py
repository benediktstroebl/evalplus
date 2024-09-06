A Python script that solves the problem of making a palindrome with the supplied tests is below:

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    if not string.startswith('a'):
        string = 'a' + string
    if not string.startswith('m'):
        string = 'mm' + string
    if not string.startswith('d'): string = 'nd' + string
    if not string.startswith('s'): string = 'ss' + string
    if not string.startswith('t'): string = 'tt' + string

    # Check the input
    if string == '':
        return ""

    # Create palindrome
    palindrome = string[::-1] + string

    return palindrome
```