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
    # Reverse the string
    reversed_string = string[::-1]
    
    # Find the longest common suffix between string and reversed_string
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # The longest palindromic suffix has been found
            break
    
    # Append to the end of string the reverse of the rest of string
    palindrome = string + reversed_string[:-len(suffix)]
    
    return palindrome


# Example use cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```