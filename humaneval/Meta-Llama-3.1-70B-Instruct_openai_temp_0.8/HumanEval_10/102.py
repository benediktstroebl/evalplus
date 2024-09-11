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

    for i in range(len(string), 0, -1):  # loop from the end of the string to the start
        postfix = string[-i:]  # get the postfix of the current length
        if is_palindrome(postfix):  # if the postfix is a palindrome
            prefix = string[:-i]  # get the prefix before the postfix
            return string + prefix[::-1]  # return the shortest palindrome

    # if no palindromic postfix is found, return the string and its reverse
    return string + string[::-1]


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines a helper function `is_palindrome` to check if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. It uses a loop to find the longest postfix of the supplied string that is a palindrome, and then appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix. If no palindromic postfix is found, it returns the string and its reverse.