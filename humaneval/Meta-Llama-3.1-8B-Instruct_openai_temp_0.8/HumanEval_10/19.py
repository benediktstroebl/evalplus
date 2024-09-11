### Python Script to Find the Shortest Palindrome that Begins with a Supplied String
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

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    palindromic_suffix = postfix
    remaining_prefix = string[:-i]
    remaining_suffix = palindromic_suffix[::-1]

    palindrome = string + remaining_suffix
    return palindrome


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```
This script defines two functions: `is_palindrome` to check if a given string is a palindrome and `make_palindrome` to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by finding the longest postfix of the supplied string that is a palindrome and then appending the reverse of the string prefix that comes before the palindromic suffix to the end of the string.