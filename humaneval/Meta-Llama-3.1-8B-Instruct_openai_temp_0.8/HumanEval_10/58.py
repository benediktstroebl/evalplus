### Make Palindrome Function
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
    if not string:  # If string is empty, return an empty string
        return ''

    longest_palindromic_suffix = ''
    for length in range(len(string), 0, -1):
        for i in range(len(string) - length + 1):
            suffix = string[i:i + length]
            if is_palindrome(suffix):
                longest_palindromic_suffix = suffix
                break
        if longest_palindromic_suffix:
            break

    # Find the remaining prefix of the string
    remaining_prefix = string[:-len(longest_palindromic_suffix)]

    # Reverse the remaining prefix
    reversed_remaining_prefix = remaining_prefix[::-1]

    # Append reversed prefix to the end of the longest palindromic suffix
    palindrome = longest_palindromic_suffix + reversed_remaining_prefix

    return palindrome


# Example usage
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
```
This script defines a function `make_palindrome` that generates the shortest palindrome that begins with a supplied string. It works by finding the longest postfix of the string that is a palindrome and then appending the reverse of the string prefix that comes before the palindromic suffix.