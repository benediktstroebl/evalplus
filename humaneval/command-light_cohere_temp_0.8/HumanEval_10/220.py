```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns: best case.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ""

    # find longest palindrome
    palindrome = ""
    for char in string:
        if char == palindrome[-1] or char == palindrome[-2]:
            palindrome += char
        else:
            break

    # reverse the prefix
    reverse = char * (len(palindrome) - 1)
    palindrome = palindrome[:0:-1] + reverse

    return palindrome
```