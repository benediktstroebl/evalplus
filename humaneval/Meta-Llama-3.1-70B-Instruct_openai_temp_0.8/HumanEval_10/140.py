```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Handle edge case for empty string
    if not string:
        return ''

    # Initialize variables to track longest palindromic suffix and the prefix before it
    longest_palindromic_suffix = ''
    prefix_before_suffix = ''

    # Iterate over string from end to start to find longest palindromic suffix
    for i in range(len(string), -1, -1):
        substr = string[i:]
        if is_palindrome(substr):
            longest_palindromic_suffix = substr
            prefix_before_suffix = string[:i]
            break

    # If string is already a palindrome, return it as is
    if not prefix_before_suffix:
        return string

    # Append reverse of prefix before suffix to the end of original string
    return string + prefix_before_suffix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```