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

    # Find the reverse of the prefix before the palindromic suffix.
    j = string.rfind(string[:i], 0, i - 1)
    if j == -1:
        return string[i:] + string[:i]
    return string[i:] + string[j+1:]
```

This code defines two functions: `is_palindrome`, which checks whether a given string is a palindrome by comparing it to its reverse, and `make_palindrome`, which takes an input string and constructs the shortest palindrome possible that starts with the input. The `make_palindrome` function achieves this by first finding the longest palindromic suffix in the input string and then determining the reverse of the prefix before this suffix. It then constructs the palindrome by concatenating the reversed prefix, the original string, and the reversed suffix. The final palindrome is returned.