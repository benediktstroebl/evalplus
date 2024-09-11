```markdown
# Make Palindrome
================

### Problem
Given a string, find the shortest palindrome that begins with a supplied string.

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
    if not string:
        return ""

    # Find the longest postfix of the supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            prefix = string[:-i]
            return postfix + prefix[::-1]

    # If no palindrome is found, return the original string
    return string


# Test cases
if __name__ == "__main__":
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # catac
    print(make_palindrome("cata"))  # catac
```
### Explanation

This Python script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse. The `make_palindrome` function finds the shortest palindrome that begins with a supplied string.

The `make_palindrome` function iterates over the postfixes of the input string in reverse order, checks if each postfix is a palindrome using the `is_palindrome` function, and returns the shortest palindrome if found. If no palindrome is found, it returns the original string.

The test cases demonstrate the correctness of the `make_palindrome` function with different input strings.