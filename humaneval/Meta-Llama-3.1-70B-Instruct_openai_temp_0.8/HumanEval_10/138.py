```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def find_longest_palindromic_suffix(string: str) -> str:
    """ Find the longest postfix of supplied string that is a palindrome """
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            return string[-i:]
    return ''


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    suffix = find_longest_palindromic_suffix(string)
    suffix_len = len(suffix)

    # If the whole string is a palindrome, return it
    if suffix_len == len(string):
        return string

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-suffix_len]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abccba'))  # 'abccba'
```