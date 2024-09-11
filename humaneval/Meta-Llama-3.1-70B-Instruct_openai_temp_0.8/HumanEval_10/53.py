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
    if not string:  # if the string is empty
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    postfix_len = 1
    while postfix_len < len(string) and not is_palindrome(string[-postfix_len:]):
        postfix_len += 1

    # If the entire string is a palindrome
    if is_palindrome(string):
        return string

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-postfix_len]
    return string + prefix[::-1]


# Test the functions
print(is_palindrome('radar'))  # True
print(is_palindrome('hello'))  # False
print(make_palindrome(''))     # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata')) # 'catac'
```

This script first defines the `is_palindrome` function to check if a given string is a palindrome. Then, the `make_palindrome` function is implemented according to the provided algorithm. Finally, the script tests both functions with example inputs.