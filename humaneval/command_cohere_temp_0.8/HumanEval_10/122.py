Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that starts with the input string."""
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix.
    suffix_start = len(string) // 2
    palindrome_suffix = string[suffix_start:][::-1]
    if string + palindrome_suffix != string[::-1]:
        return make_palindrome(string + palindrome_suffix)
    # Find the shortest non-palindrome prefix of the string right before the palindrome suffix.
    for i in range(suffix_start - 1, -1, -1):
        if string[i] != string[i + (2 * (len(string) - suffix_start))]]:
            break
    else:
        i = -1
    # Create the new string by concatenating the reverse of the non-palindrome prefix,
    # the original string, and the palindrome suffix.
    new_string = string[i + 1:][::-1] + string + palindrome_suffix
    return make_palindrome(new_string)
```

This script includes the `is_palindrome` function, which is an essential part of the `make_palindrome` algorithm. The `make_palindrome` function uses the palindrome checking function to recursively find the shortest palindrome that begins with the supplied string. The algorithm works by finding the longest postfix of the input string that is a palindrome. It then appends the reverse of the shortest non-palindromic string that comes before the palindromic suffix to the end of the string. The result is a new string that is a palindrome if possible, and the algorithm repeats until the goal is achieved. 

Note that the script assumes that the input string is composed only of lowercase letters. You can modify the script to handle uppercase letters and non-alphabetical characters by accounting for those characters in the palindrome checking function. Incorporate the above code into a Python module, bin for pal, with corresponding test cases to ensure proper functionality:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that starts with the input string."""
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix.
    suffix_start = len(string) // 2
    palindrome_suffix = string[suffix_start:][::-1]
    if string + palindrome_suffix != string[::-1]:
        return make_palindrome(string + palindrome_suffix)
    # Find the shortest non-palindrome prefix of the string right before the palindrome suffix.
    for i in range(suffix_start - 1, -1, -1):
        if string[i] != string[i + (2 * (len(string) - suffix_start))]]:
            break
    else:
        i = -1
    # Create