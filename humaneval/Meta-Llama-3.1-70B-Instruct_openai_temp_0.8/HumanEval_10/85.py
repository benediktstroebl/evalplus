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
    # Handle edge case where string is empty
    if not string:
        return ''

    # Initialize variables
    longest_palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        # Check if the current suffix is a palindrome
        if is_palindrome(string[i-1:]):
            longest_palindromic_suffix = string[i-1:]
            break

    # Calculate the prefix to be appended
    prefix_to_append = string[:len(string) - len(longest_palindromic_suffix)]
    reversed_prefix = prefix_to_append[::-1]

    # Return the shortest palindrome
    return string + reversed_prefix


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abcd'))  # 'abcdcba'
```