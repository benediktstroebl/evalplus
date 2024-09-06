Here is a Python script with a self-contained function that solves the problem of creating a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Find the longest postfix of the string that is a palindrome
    palindrome = string[:][::-1].count(str.ispalind

    max_palindrome = len(string) - len(str.count(palindrome))
    return palindrome + str(max_palindrome)
```

This script provides a function to determine if a given string is a palindrome and another function to generate the shortest palindrome from a given string.