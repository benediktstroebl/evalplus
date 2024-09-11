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
    
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            palindrome = string + postfix[::-1]
            return palindrome
            
    # If no palindrome postfix is found, return the original string (which is a palindrome itself)
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This Python script defines two functions, `is_palindrome` and `make_palindrome`, as specified in the problem description. The `is_palindrome` function checks if a given string is a palindrome, and the `make_palindrome` function generates the shortest palindrome that begins with a supplied string. The test cases at the end demonstrate the usage of the `make_palindrome` function.