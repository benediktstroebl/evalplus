```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Reverse the string
    rev_string = string[::-1]
    
    # Iterate through the reversed string to find the longest postfix that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Append the reverse of the prefix to the string
            return string + rev_string[:i]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines two functions: `is_palindrome` checks whether a string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with a supplied string.

The `make_palindrome` function works by first reversing the input string. Then it iterates through the reversed string to find the longest postfix that is a palindrome. Once it finds the longest palindromic postfix, it appends the reverse of the prefix to the original string to form the shortest palindrome.