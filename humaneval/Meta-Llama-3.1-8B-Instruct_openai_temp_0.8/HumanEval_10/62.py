### Code

```markdown
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
    
    # If the string is already a palindrome, return it as is
    if is_palindrome(string):
        return string
    
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[i-1::-1]
    
    # If no palindrome postfix is found, return the original string
    return string


# Test the function
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: "catac"
print(make_palindrome("cata"))  # Output: "catac"
print(make_palindrome("abc"))  # Output: "abcba"
```

### Explanation

The script defines two functions: `is_palindrome` and `make_palindrome`. 

- `is_palindrome` checks if a given string is a palindrome by comparing it to its reverse.
- `make_palindrome` finds the shortest palindrome that begins with a supplied string by finding the longest postfix of the supplied string that is a palindrome, appending to the end of the string reverse of a string prefix that comes before the palindromic suffix.

The `make_palindrome` function uses a loop to find the longest postfix of the supplied string that is a palindrome. If a palindrome postfix is found, the function appends to the end of the string reverse of a string prefix that comes before the palindromic suffix. If no palindrome postfix is found, the function returns the original string.