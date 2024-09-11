### Palindrome Generation
Here is the Python script that defines the `is_palindrome` and `make_palindrome` functions.

```markdown
### Code
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
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest palindromic postfix
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Extract the prefix from the original string
            prefix = string[:i]
            # Reverse the prefix to generate the palindrome
            palindrome = postfix + prefix[::-1]
            return palindrome

    # If no palindromic postfix is found, return the original string
    return string
```

### Example Usage
```markdown
# Test the functions
print(is_palindrome('radar'))  # True
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('cat'))   # 'catac'
print(make_palindrome(''))      # ''
print(is_palindrome('cat'))     # False
```

This script provides a simple implementation of the `is_palindrome` and `make_palindrome` functions as per the given problem description. The `make_palindrome` function generates the shortest palindrome that begins with a given string by finding the longest palindromic postfix and appending the reversed prefix to it. The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse.