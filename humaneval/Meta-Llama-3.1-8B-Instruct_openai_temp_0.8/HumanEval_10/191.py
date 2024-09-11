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
    # Check if the input string is empty
    if not string:
        return ''

    # Reverse the input string to simplify the algorithm
    reversed_string = string[::-1]

    # Initialize a suffix pointer and a prefix pointer
    suffix_idx = 0
    prefix_idx = 0

    # Loop until the suffix pointer meets the prefix pointer
    while suffix_idx < len(string) and prefix_idx < len(reversed_string):
        # If the characters match, move both pointers forward
        if string[suffix_idx] == reversed_string[prefix_idx]:
            suffix_idx += 1
            prefix_idx += 1
        # If the characters do not match, move the prefix pointer forward
        else:
            prefix_idx += 1

    # The suffix pointer is now one position before the palindromic suffix
    palindromic_suffix_len = suffix_idx

    # If the input string is a palindrome, return the original string with a 'c' in the middle
    if palindromic_suffix_len == len(string):
        return string + 'c' + string[::-1]

    # Otherwise, return the input string followed by the reverse of its prefix
    return string + reversed_string[prefix_idx:]


# Example usage
print(is_palindrome('radar'))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(make_palindrome(''))
```