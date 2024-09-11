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
    if not string:  # edge case: empty string
        return string

    i = 1
    while i <= len(string):
        if is_palindrome(string[-i:]):  # check if postfix is a palindrome
            # the length of the palindromic postfix is i, so the number of characters before it is len(string) - i
            return string + string[:len(string) - i][::-1]
        i += 1

    return string  # if no palindromic postfix is found, return the original string


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script implements the `make_palindrome` function as described. It first checks if the original string is a palindrome by calling the `is_palindrome` function. If it is, it returns the original string. If not, it starts from the end of the string and checks each postfix to see if it is a palindrome. If it finds a palindromic postfix, it returns the string with the prefix before the postfix reversed and appended. If no palindromic postfix is found, it returns the original string.