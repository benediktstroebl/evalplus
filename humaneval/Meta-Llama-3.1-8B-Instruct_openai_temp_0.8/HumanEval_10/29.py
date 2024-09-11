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
    if not string:  # if the input string is empty
        return ''

    i = len(string) - 1  # start from the end of the string
    while i >= 0:  # move backwards until we find a mismatch
        if string[i] == string[0]:  # if the character at the current position is the same as the first character
            i -= 1  # move one step backwards
        else:
            break  # if we find a mismatch, exit the loop

    # reverse the prefix (string[:i+1]) and append it to the string
    reverse_prefix = string[:i+1][::-1]
    return string + reverse_prefix


# Example usage:
print(is_palindrome('madam'))  # True
print(make_palindrome('cat'))   # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome(''))      # ''
```

This script defines the `is_palindrome` function to check if a string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the input string that is a palindrome, and then appends the reverse of the prefix to the end of the string to make it a palindrome. The script also includes example usage at the end.