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
    # Start with the entire string as a potential palindrome
    for length in range(len(string), 0, -1):
        # Extract a postfix of the current length
        postfix = string[-length:]
        
        # Check if the postfix is a palindrome
        if is_palindrome(postfix):
            # If it is, append the reverse of the prefix to the end of the string
            prefix = string[:-length]
            return string + prefix[::-1]

    # If no palindromic postfix is found, return the string followed by its reverse
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
```