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
    if not string:  # If the string is empty, return it
        return string
    
    palindromic_suffix = ''  # Initialize the longest palindromic suffix
    i = len(string) - 1  # Start from the end of the string
    
    while i >= 0:  # Check each postfix of the string
        if string[:i+1] == string[:i+1][::-1]:  # If the postfix is a palindrome
            palindromic_suffix = string[:i+1]  # Update the longest palindromic suffix
        i -= 1  # Move to the previous character
    
    # Append the reverse of the prefix before the palindromic suffix to make the string a palindrome
    return string + string[:len(string) - len(palindromic_suffix)][::-1]


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```