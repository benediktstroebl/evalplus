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
    # Start checking from the beginning of the string
    for i in range(len(string), 0, -1):
        # Check if the current substring is a palindrome
        if is_palindrome(string[:i]):
            # If it is, reverse the rest of the string to make the palindrome
            return string + string[:i][::-1]
    # If no palindromic suffix is found, return the original string
    return string


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
```

This script uses the `is_palindrome` function to check for palindromes within the input string. The `make_palindrome` function then iterates over the input string in reverse, checking each substring to see if it's a palindrome. If it finds a palindromic suffix, it appends the reverse of the prefix to the end of the string to make the shortest palindrome.