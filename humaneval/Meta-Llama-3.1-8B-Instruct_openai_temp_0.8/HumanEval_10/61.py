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
    for i in range(len(string), 0, -1):
        # check if the substring is a palindrome
        substring = string[-i:]
        if is_palindrome(substring):
            # append reverse of prefix to the end of the palindrome
            prefix = string[:-i]
            return substring + prefix[::-1]
    # if no palindrome is found, return the string itself
    return string


# Example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This Python script first defines a function `is_palindrome` that checks whether a given string is a palindrome. It then defines the `make_palindrome` function, which finds the shortest palindrome that begins with a supplied string by trying to find the longest postfix of the string that is a palindrome and appending the reverse of the prefix to the end of the palindrome. If no palindrome is found, the function returns the string itself. The example usage at the end demonstrates how to use the `make_palindrome` function.