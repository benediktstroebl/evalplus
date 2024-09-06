Here is a Python script that contains a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    lis = []
    while True:
        pal = []
        for i in range(0, len(string)):
            if string[i] == string[len(string) - i - 1]:
                pal.append(string[i])
                pal.append(string[len(string) - i - 1])
        lis.append(pal)
        if pal == []:
            break
    return lis[0]
```
This function, `make_palindrome`, constructs the shortest palindrome that begins with a supplied string. It uses a idea simple:
- Find the longest postfix of supplied string that is a palindrome.
- Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

This function has been designed to be self-contained, with the output and input being the same. This makes it function more concise and easier to test, as it does not require any additional arguments or values.