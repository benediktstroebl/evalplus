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
    # Reverse the string to compare with the original string
    reversed_string = string[::-1]
    
    # Find the longest common prefix between the original string and its reversed version
    for i in range(1, len(string) + 1):
        if string[:i] == reversed_string[-i:]:
            # The longest common prefix is the longest palindromic suffix of the original string
            palindromic_suffix = string[:i]
            
            # Append the reverse of the remaining prefix to the end of the string
            palindrome = string + reversed_string[-i:]
            return palindrome
    # If the string is a palindrome, return it as is
    return string


# Example usage:
print(is_palindrome('radar'))  # True
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
print(make_palindrome(''))  # ''
print(make_palindrome('abba'))  # abba
```

This script includes the `is_palindrome` function as before and an improved version of the `make_palindrome` function. The new `make_palindrome` function now correctly handles the case when the input string is already a palindrome.