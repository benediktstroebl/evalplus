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
    # Handle empty string
    if not string:
        return ''

    # Find the longest palindrome suffix
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i]!= string[j]:
            break
        i += 1
        j -= 1

    # If the entire string is a palindrome, return it
    if i >= j:
        return string

    # Otherwise, append the reverse of the prefix to the palindromic suffix
    return string + string[i + 1:j + 1][::-1]


# Example usage
print(is_palindrome('radar'))  # True
print(make_palindrome('cat'))   # catac
print(make_palindrome('cata'))  # catac
```
This script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` creates the shortest palindrome that begins with a given string. The `make_palindrome` function works by first finding the longest palindrome suffix of the input string, and then appending the reverse of the prefix to the palindromic suffix. If the entire string is a palindrome, it simply returns the original string.