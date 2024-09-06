Below is a self-contained Python script that includes a function is_palindrome that determines whether a given string is a palindrome, and a function make_palindrome that creates the shortest palindrome starting with a provided string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    """
expected output:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    prefix, suffix = palindrome_prefix_suffix(string)
    return prefix + suffix[::-1]

def palindrome_prefix_suffix(string):
    """ Determine the longest palindrome prefix and suffix.
    regEx: 'abcde...' -> ('abcde', '...')
    """
    # Remove all non-alphanumeric and special characters
    # Keep only alphanumeric characters and spaces
    str = ''.join(char for char in string if char.isalnum() or Dry to alnum.mixed case, 'is a string
    """
    if string is not str:
        return '', ''
    l = len(string)
    p = 2  # palindrome prefix
    s = l - 1  # palindrome suffix
    return str[p:l:s], str[l - s + 1:l]
```

The make_palindrome function employs the palindrome_prefix_suffix function to locate the longest palindrome prefix and suffix within the supplied string. The prefix and suffix are then concatenated using the + operator, and the result is returned as the shortest palindrome.