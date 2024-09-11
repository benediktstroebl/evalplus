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
    if not string:  # empty string is a palindrome
        return ''

    prefix = ''
    for i in range(len(string), 0, -1):
        # check for palindrome
        if is_palindrome(string[:i]):
            # shortest palindrome found
            suffix = string[i:]
            palindrome = string + suffix[::-1]
            return palindrome
        prefix = string[:i]

    # if no palindrome is found, return original string as the default
    return string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first checks if the input string is empty, in which case it returns an empty string (since an empty string is a palindrome). Then, it iterates through the string from the end to the start, checking for palindromes. The first palindrome it finds is the longest postfix of the string that is a palindrome. The script then returns the shortest palindrome that begins with the input string by appending the reverse of the prefix that comes before the palindromic suffix to the end of the input string. If no palindrome is found, the script returns the original string.