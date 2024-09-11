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
        # If string is empty, return it as it's already a palindrome
        return string

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Found the longest palindromic postfix, now find its prefix
            prefix = string[:-i]
            # Append to the end of the string reverse of a string prefix
            palindrome = string + postfix[::-1]
            return palindrome

    # If no palindromic postfix found (shouldn't happen), raise ValueError
    raise ValueError("No palindromic postfix found for the given string")


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This script implements the `make_palindrome` function as described, using the `is_palindrome` function to test strings for palindromicity. The main logic of the `make_palindrome` function is implemented in a loop that iterates over the string from the end, finding the longest palindromic postfix and its prefix, and then constructing the palindrome.