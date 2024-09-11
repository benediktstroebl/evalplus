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
    rev_string = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(string + rev_string[i:]):
            return string + rev_string[i:]
    return string + rev_string


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome('abcddcba'))  # Output: 'abcddcba'
print(make_palindrome('abccba'))  # Output: 'abccba'
print(make_palindrome('abcd'))  # Output: 'abcdcba'
```