```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    palindromic_start = len(string) // 2
    while not is_palindrome(string[palindromic_start:]):
        palindromic_start -= 1

    reversed_prefix = string[::-1][::-1][1:]
    return string[:palindromic_start] + reversed_prefix
```

This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` creates a palindrome from a given string. The `make_palindrome` function iteratively searches for the longest postfix of the string that is a palindrome and then constructs the palindrome by appending the reversed prefix to the end of the original string.