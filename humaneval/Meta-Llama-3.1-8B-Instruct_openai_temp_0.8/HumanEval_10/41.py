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
    # Reverse the string to easily check if a suffix is a palindrome
    rev_string = string[::-1]
    
    # Iterate over the reversed string
    for i in range(len(string)):
        # Check if the suffix starting at current index is a palindrome
        if is_palindrome(rev_string[i:]):
            # If it is, append the reverse of the prefix to the end of the string
            return string + rev_string[:i][::-1]
    
    # If no palindromic suffix is found, return the original string
    return string


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first defines the `is_palindrome` function to check if a string is a palindrome. Then it defines the `make_palindrome` function, which finds the longest palindromic suffix of the string and appends to it the reverse of the string prefix that comes before the palindromic suffix. If no such suffix is found, it returns the original string.