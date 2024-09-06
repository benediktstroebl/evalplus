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
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # Find the shortest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    # Return the palindrome concatenated with the reverse of the non-palindromic prefix.
    return make_palindrome(string[j:i][::-1]) + string[j:]
``` 

The `make_palindrome()` function efficiently identifies the longest palindromic suffix of the supplied string and then constructs the shortest palindrome by concatenating it with the reverse of the corresponding non-palindromic prefix. The `is_palindrome()` function serves as an auxiliary helper to test if a substring is a palindrome.