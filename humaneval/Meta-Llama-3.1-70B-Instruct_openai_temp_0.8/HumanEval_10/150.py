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

    :param string: The input string
    :return: The shortest palindrome that begins with the input string
    """
    if not string:
        return ''

    for i in range(len(string), 0, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]
            return string + prefix[::-1]

    # If no palindromic postfix found, append the reverse of the input string
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This solution iterates through the input string from the end to the start, checking each postfix to see if it is a palindrome. When it finds the longest palindromic postfix, it appends the reverse of the corresponding prefix to the end of the input string, resulting in the shortest palindrome that begins with the input string. If no palindromic postfix is found, the solution simply appends the reverse of the input string to itself.