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
    if not string:  # if string is empty, return it immediately
        return string
    
    for i in range(len(string), 0, -1):  # find the longest palindromic postfix
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]  # get the prefix before the palindromic postfix
            return string + prefix[::-1]  # append reverse of prefix to the end of the string


# example usage
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```