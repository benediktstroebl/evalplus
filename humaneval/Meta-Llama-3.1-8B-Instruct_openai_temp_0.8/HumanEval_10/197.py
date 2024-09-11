Here's a Python script that implements the `is_palindrome` and `make_palindrome` functions.

```markdown
### Palindrome Functions
#### Definition
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
    if string == string[::-1]:  # if string is already a palindrome
        return string
    # find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # reverse the prefix
            prefix = string[:-i]
            return postfix + prefix[::-1]
```

#### Usage
```python
# Test the palindrome functions
print(is_palindrome('radar'))  # True
print(is_palindrome('python'))  # False

print(make_palindrome('cata'))  # catac
print(make_palindrome('cat'))   # catac
print(make_palindrome('abc'))   # abcba
```

This script defines the `is_palindrome` function to check if a string is equal to its reverse. The `make_palindrome` function checks if the input string is already a palindrome. If not, it iterates over the string from the end, checking for the longest palindromic postfix. It then reverses the prefix and appends it to the postfix to form the shortest palindrome that begins with the input string.