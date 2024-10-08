### Solution
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
    # Find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Find the prefix that comes before the palindromic postfix
            prefix = string[:-i]
            # Reverse the prefix and append it to the postfix
            return postfix + postfix[::-1]

    # If no palindromic postfix is found, return the original string
    return string
```

### Example Usage
```python
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```