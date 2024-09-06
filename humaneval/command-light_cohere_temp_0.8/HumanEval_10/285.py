Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns: a problem description."""
    palindrome = ""
    l = 0
    while l < len(string) - 1:
        if string[l] == string[l + 1]:
            l += 2
        else:
            palindrome = palindrome + string[l] + string[l + 1]
            l = l + 2
    return palindrome[::-1]
```

This code provides a function `is_palindrome` that checks if a given string is a palindrome and the `make_palindrome` function that generates the shortest palindrome given a string.

The `make_palindrome` function uses a simple algorithm to generate the palindrome, by checking if the next character is the same as the previous one or not, and if not, appending it to the palindrome. The function then reverses the final part of the string to return the palindrome.