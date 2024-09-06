Below is a Python script that includes a self-contained function `make_palindrome(string)` that solves the problem of creating a palindrome of a given string.

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:  # empty string
        return ''
    palindrome = []
    while True:
        palindrome.append(string[0])
        while len(string) > 1 and string[-1] == palindrome[-1]:
            string = string[:-1] + string[-1:]
        else:
            break
    return ''.join(palindrome)
```
The function works by creating an empty list `palindrome` and then iterates over the string, appending each character to the list if it is the first occurrence of a palindrome. The function ensures that it appends the character only when it is a palindrome, by checking if the character and the previous character are the same. The function then joins the palindrome characters to get the shortest palindrome.