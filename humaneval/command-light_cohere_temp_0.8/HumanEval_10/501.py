```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[: len(string) // 2] + string[-1:]
    return palindrome
```

This code defines two functions: `is_palindrome` checks if a given string is a palindrome, while `make_palindrome` finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses the `is_palindrome` function to check if the input string is a palindrome, and if not, it returns an empty string. The function works by:
1. If the input string is a palindrome, it returns the input string as it is.
2. Otherwise, it tries to create a palindrome using the algorithm idea of finding the longest postfix of the string that is a palindrome and appending it to the reverse of a string prefix that comes before the palindrome.