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
    if not string:  # Base case: Empty string
        return ''

    longest_postfix = ''
    for i in range(len(string), 0, -1):  # Iterate over postfixes from longest to shortest
        postfix = string[-i:]  # Get the current postfix
        if is_palindrome(postfix):  # Check if it's a palindrome
            longest_postfix = postfix  # Update the longest palindromic postfix
            break

    prefix = string[:-len(longest_postfix)]  # Get the prefix that comes before the longest palindromic postfix
    return string + prefix[::-1]  # Append the reverse of the prefix to the end of the string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This script defines two functions, `is_palindrome` and `make_palindrome`, which work together to find the shortest palindrome that begins with a given string. The `make_palindrome` function iterates over postfixes of the input string from longest to shortest, checking if each one is a palindrome. When it finds the longest palindromic postfix, it appends the reverse of the corresponding prefix to the end of the string to form the shortest palindrome.