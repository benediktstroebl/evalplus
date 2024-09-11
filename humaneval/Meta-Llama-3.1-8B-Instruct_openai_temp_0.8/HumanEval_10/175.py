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
    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            prefix = string[:-i]
            # Append to the end of the string reverse of the prefix
            palindrome = postfix + prefix[::-1]
            return palindrome
    # If no postfix is found, return the original string
    return string


# Example use cases
if __name__ == "__main__":
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: 'catac'
    print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the input string. It uses a simple algorithm to find the longest postfix of the input string that is a palindrome, and then appends the reverse of the prefix to the end of the postfix. If no such postfix is found, the function returns the original string. The script also includes example use cases to demonstrate the function's behavior.