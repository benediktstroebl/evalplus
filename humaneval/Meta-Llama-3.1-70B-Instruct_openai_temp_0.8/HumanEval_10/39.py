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
    if not string:
        return ''
    
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]
            return string + prefix[::-1]
    
    # If no palindromic postfix is found, append the reverse of the entire string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This script defines two functions, `is_palindrome` and `make_palindrome`, and includes test cases to validate its correctness. The `make_palindrome` function iterates over the string from the end to the beginning, checking each postfix to see if it's a palindrome. When it finds a palindromic postfix, it appends the reverse of the corresponding prefix to the end of the string and returns the result. If no palindromic postfix is found, it simply appends the reverse of the entire string.