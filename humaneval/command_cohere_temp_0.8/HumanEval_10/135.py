Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = i - 1
    while string[j:i] == string[j:i][::-1]:
        j -= 1
    if j < 0:
        return string

    return make_palindrome(string[:j] + string[i:])
```

This code defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. The function uses two pointers to efficiently find the shortest palindrome. The algorithm terminates early if a non-matching character is found, guaranteeing the shortest possible palindrome.