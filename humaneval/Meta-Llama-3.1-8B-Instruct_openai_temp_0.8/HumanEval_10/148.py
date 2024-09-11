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
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    postfix_index = len(string) - 1
    while postfix_index >= 0 and string[postfix_index]!= string[0]:
        postfix_index -= 1

    # If no palindrome postfix is found, return the original string with 'a' appended
    if postfix_index < 0:
        return string + 'a'

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:postfix_index + 1]
    return string + prefix[::-1]


# Example usage:
print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
```
In this script, the `make_palindrome` function finds the longest postfix of the input string that is a palindrome by iterating from the end of the string backwards and checking if the current character matches the first character of the string. If a palindrome postfix is found, it appends the reverse of the prefix before the palindrome to the end of the string to create the shortest palindrome.