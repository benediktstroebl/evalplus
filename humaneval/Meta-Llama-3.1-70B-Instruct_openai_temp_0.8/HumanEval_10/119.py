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
    if not string:  # if string is empty
        return string
    
    for i in range(len(string) - 1, -1, -1):  # iterate from the end to the start
        postfix = string[i:]  # get the postfix
        if is_palindrome(postfix):  # check if the postfix is a palindrome
            prefix = string[:i]  # get the prefix
            return string + prefix[::-1]  # return the shortest palindrome

    return string + string[::-1]  # if no palindromic postfix is found, append the reverse of the whole string


# Test cases
print(make_palindrome(''))  # Should print ''
print(make_palindrome('cat'))  # Should print 'catac'
print(make_palindrome('cata'))  # Should print 'catac'
```

This script first checks if the input string is empty. If it is, it returns the empty string. Then it iterates over the string from the end to the start, checking each postfix to see if it is a palindrome. If a palindromic postfix is found, it returns the original string plus the reverse of the prefix that comes before the palindromic suffix. If no palindromic postfix is found, it returns the original string plus its reverse. This solution ensures that the resulting palindrome is the shortest possible one that begins with the supplied string.