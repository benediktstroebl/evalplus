```markdown
### Palindrome Problem Solution

#### Problem Description

Create a function `make_palindrome` that accepts a string as input and returns the shortest palindrome that begins with the supplied string. The function uses the `is_palindrome` helper function to check if a string is a palindrome.

#### Code

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

    Args:
    string (str): The input string.

    Returns:
    str: The shortest palindrome that begins with the supplied string.

    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # If the string is a palindrome, it is the shortest palindrome
    if is_palindrome(string):
        return string

    # Check for palindromes in postfixes
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        # If postfix is a palindrome, append reverse of prefix to postfix
        if is_palindrome(postfix):
            return string + postfix[::-1]

    # If no palindrome was found, return the original string
    return string
```

#### Example Use Cases

```python
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```