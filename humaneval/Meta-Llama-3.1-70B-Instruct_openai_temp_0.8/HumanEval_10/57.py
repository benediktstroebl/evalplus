```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def find_longest_palindromic_suffix(string: str) -> str:
    """ Find the longest postfix of supplied string that is a palindrome """
    for i in range(len(string), 0, -1):
        suffix = string[i-1:]
        if is_palindrome(suffix):
            return suffix
    return ''


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
    if is_palindrome(string):
        return string
    
    palindromic_suffix = find_longest_palindromic_suffix(string)
    
    if palindromic_suffix:
        prefix = string[:-len(palindromic_suffix)]
        return string + prefix[::-1]
    else:
        return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```