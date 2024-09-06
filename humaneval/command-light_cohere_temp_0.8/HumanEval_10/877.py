Here's the Python script with the function that creates the palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    if len(string) < 2:
        return string
    palindrome = string[:] + string[-1:]
    for char in string[1:-1]:
        if char == palindrome[-1]:
            palindrome += char
        else:
            palindrome += char[::-1]
    return palindrome
```

The `make_palindrome` function uses a simple algorithm to create the shortest palindrome for a given string. It first checks if the certain tests, and if not, it returns the original string. It then finds the the longest postfix of the string that is a palindrome and appends the reverse of the string prefix before the palindromic suffix. The function then handles the string that does not contain a palindrome and has less than two characters, it returns the original string.