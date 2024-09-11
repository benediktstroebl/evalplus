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
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), -1, -1):  # start from the end of string
        if is_palindrome(string[i:]):  # find the longest postfix that is a palindrome
            prefix = string[:i]  # find the prefix that comes before the palindromic suffix
            return string + prefix[::-1]  # append the reverse of the prefix to the end of the string


# test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('race'))  # 'racecar'
print(make_palindrome('radar'))  # 'radar'
```