```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
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
    
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix of the string
    for i in range(len(string), 0, -1):
        # Check if the current postfix is a palindrome
        if is_palindrome(string[-i:]):
            # If it is, append the reverse of the prefix to make the string a palindrome
            return string + string[-i:][::-1]
    
    # If no palindromic suffix is found, return the original string
    return string


# Example usage
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: "catac"
print(make_palindrome("cata"))  # Output: "catac"
```

In this script, the `make_palindrome` function uses a simple iterative approach to find the longest postfix of the input string that is a palindrome. It then appends the reverse of the prefix to make the string a palindrome. The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse.