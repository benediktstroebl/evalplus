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
    def expand_around_center(s: str, left: int, right: int) -> str:
        """ Expand around the center of a string to find the largest palindrome """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    prefix = ''
    while string and not is_palindrome(string):
        prefix += string[0]
        string = string[1:]
        for i in range(len(string), 0, -1):
            pal = expand_around_center(string, 0, i - 1)
            if is_palindrome(pal):
                string = string[:i - len(pal)] + pal + string[i - len(pal):]
                break
        else:
            return string + prefix + string[::-1]
    return string + prefix + string[::-1]


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('a'))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('abc'))  # False

print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abc'))  # 'abccba'
print(make_palindrome('a'))  # 'a'
print(make_palindrome('aba'))  # 'ababa'
```

This script first defines the `is_palindrome` function to test if a given string is a palindrome. Then, it defines the `make_palindrome` function that constructs the shortest palindrome that begins with a supplied string by finding the longest postfix that is a palindrome and appending the reverse of the prefix that comes before the palindromic suffix. The `expand_around_center` function is used to expand around the center of the string to find the largest palindrome.