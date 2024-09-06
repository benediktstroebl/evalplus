Here is a self-contained Python function that solves the problem of finding the shortest palindrome of a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    palindrome = []
    while True:
        palindrome.append(char)
        if char == palindrome[-1]:
            break
        char = char[::-1]
    return ''.join(palindrome)
```
The function starts with an empty string, then appends characters to the string until it encounters its reverse (which is a palindrome) and breaks the loop. This effectively constructs the class shortest palindrome.