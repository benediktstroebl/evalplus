### Shortest Palindrome Finder Script
#### Python script that checks if a string is a palindrome and generates the shortest palindrome

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
    """
    if not string:
        return ''

    # Find the longest postfix that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            return string + string[:-i][::-1]

    # If no palindromic postfix found, use the entire string as the prefix
    return string + string[1:][::-1]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

In this script, we define two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest postfix of the supplied string that is a palindrome and appends the reverse of the prefix to the end of the string. If no palindromic postfix is found, it uses the entire string as the prefix.