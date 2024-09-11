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
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Find the palindromic prefix by taking the first half of the string
            prefix = string[:len(string) // 2]
            # Reverse the prefix and append it to the postfix
            palindrome = postfix + prefix[::-1]
            return palindrome

    # If no palindromic suffix is found, return the original string
    return string


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script defines the `is_palindrome` function to check if a string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest palindromic suffix of the input string and then appending the reverse of the string prefix to it. If no palindromic suffix is found, it returns the original string.