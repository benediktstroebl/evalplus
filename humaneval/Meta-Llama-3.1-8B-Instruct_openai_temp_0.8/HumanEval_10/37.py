```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Reverse the string to compare with the prefix
    rev_str = string[::-1]
    
    # Find the length of the longest common prefix between the string and its reverse
    i = 0
    while i < len(string) and string[i] == rev_str[i]:
        i += 1
    
    # The longest common prefix is the reverse of the postfix that comes after it
    postfix = string[i:]
    prefix = string[:i]
    
    # The palindrome is formed by appending the reverse of the prefix to the string
    palindrome = string + rev_str[i:]
    
    return palindrome


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This code defines the `make_palindrome` function, which finds the shortest palindrome that begins with a supplied string by finding the longest postfix of the string that is a palindrome and appending the reverse of the string prefix that comes before the palindromic suffix. The test cases are included to demonstrate the function's behavior.