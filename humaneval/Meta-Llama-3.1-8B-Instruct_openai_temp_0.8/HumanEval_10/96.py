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
    # Check if input string is empty
    if not string:
        return ''

    # Find the longest palindromic suffix of the string
    longest_palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        substr = string[-i:]
        if is_palindrome(substr):
            longest_palindromic_suffix = substr
            break

    # Find the prefix of the string that comes before the palindromic suffix
    prefix = string[:-len(longest_palindromic_suffix)]

    # Reverse the prefix and append it to the end of the string
    palindrome = string + prefix[::-1]

    return palindrome


# Test the function
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This script first defines a helper function `is_palindrome` to check if a given string is a palindrome. Then it defines the `make_palindrome` function, which finds the longest palindromic suffix of the input string, finds the prefix that comes before it, and appends the reversed prefix to the end of the string to make it a palindrome. The script includes some test cases to verify the correctness of the `make_palindrome` function.