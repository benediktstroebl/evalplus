Here is a self-contained Python script with a function that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """ Returns example code that using list comprehension to find the longest palindrome and reverse of a string prefix.
    """
    longest_palindrome = [i for i, palindrome in enumerate(string[::-1], 1) if palindrome == string[i:][::-1]]
    return string[:len(longest_palindrome)] + longest_palindrome[::-1] + string[len(longest_palindrome):]
```

This function takes a string as input and returns a boolean value indicating whether the input string is a palindrome, and a string that is the shortest palindrome that begins with the input string.