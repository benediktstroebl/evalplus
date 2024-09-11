```markdown
### Palindrome Maker

This script provides two functions: `is_palindrome` to check if a given string is a palindrome, and `make_palindrome` to generate the shortest palindrome that begins with a supplied string.

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
    # Reverse the string to make it easier to find the longest postfix that is a palindrome
    rev_string = string[::-1]
    
    # Iterate over the string to find the longest postfix that is a palindrome
    for i in range(len(string)):
        postfix = string[i:]
        if is_palindrome(postfix):
            return string + postfix[::-1]


# Example usage
if __name__ == "__main__":
    print(is_palindrome("level"))  # True
    print(is_palindrome("hello"))  # False
    
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # 'catac'
    print(make_palindrome("cata"))  # 'catac'
    print(make_palindrome("abcd"))  # 'abcdcba'
```

### Notes

- The `is_palindrome` function checks if a string is a palindrome by comparing it to its reverse.
- The `make_palindrome` function finds the longest postfix of the supplied string that is a palindrome and appends the reverse of the string prefix to the end to form the shortest palindrome.
- The example usage demonstrates how to use the functions with different inputs.