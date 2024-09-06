Here is a self-contained Python script that defines a function is_palindrome that checks if a given string is a palindrome:
```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:string.rindr: len(string) - 1]
    return palindrome + palindrome[::-1]
```

This script has a function to check if a given string is a palindrome and another function to generate the shortest palindrome that begins with a supplied string.