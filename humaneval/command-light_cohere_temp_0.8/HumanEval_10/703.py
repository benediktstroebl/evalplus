```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest palindrome suffix
    palindrome_suffix = find_palindrome_suffix(string)

    # Append the palindrome suffix to the original string in reverse order
    return string + palindrome_suffix[::-1]

def find_palindrome_suffix(string):
    # Remove all non-alphanumeric characters and convert to lowercase
    clean_string = ''.join.join(char.lower() for c if char in string for c in string)

    # Find the length of the longest palindrome
    max_length = 0
    for len_str in range(1, len(clean_string) + 1):
        if is_palindrome(clean_string[:len_str]):
            max_length = max(len_str)

    return clean_string[-max_length:]
```
This code implements a solution to the problem of checking if a given string is a palindrome and constructing a palindrome from a given string. The code is organized into separate functions for readability and maintainability.