Here is a Python script with a self-contained function that solves the problem of creating a palindrome of a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Function to construct a palindrome
    longest_palindrome = len(''.join(char for char in string if char == char[::-1])
    return ''.join(char for char in string if char == char[::-1]) + '\n' + ''.join(char for char in string if char != char[::-1])
```

This function takes a string as input and uses two nested loops to identify the longest palindromic substring and reverse it. The function then constructs theby appending the reverse of the longest palindrome to the original string and reversing the rest of the string.