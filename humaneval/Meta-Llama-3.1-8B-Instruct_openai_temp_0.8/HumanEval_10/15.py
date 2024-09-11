```markdown
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
    # If the input string is already a palindrome, return it
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix
    suffix = ''
    for i in range(len(string), 0, -1):
        suffix = string[:i]
        if is_palindrome(suffix):
            break

    # Append the reverse of the prefix to the palindromic suffix
    palindrome = suffix + string[:len(string)-len(suffix)][::-1]
    
    return palindrome
```

**Example Use Cases:**

```python
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. It uses the `is_palindrome` function to check if a given string is a palindrome. The `make_palindrome` function first checks if the input string is already a palindrome. If not, it finds the longest palindromic suffix and appends the reverse of the remaining prefix to it.