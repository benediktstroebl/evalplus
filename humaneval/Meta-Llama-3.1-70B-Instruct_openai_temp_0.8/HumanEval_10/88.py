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
    
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # Expected output: ''
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('race'))  # Expected output: 'racecar'
print(make_palindrome('radar'))  # Expected output: 'radar'
```

In the provided script, we define two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that starts with the input string.

The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix. If no such palindrome is found, it simply appends the reverse of the entire string.

This solution has a time complexity of O(n^2) due to the string reversal operation inside the loop. However, it is straightforward to implement and easy to understand.