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
    
    :param string: Input string
    :return: Shortest palindrome that begins with the input string
    """
    if not string:
        return ''

    # Start from the end of the string and find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Append the reverse of the prefix to the end of the string
            return string + string[:i][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```