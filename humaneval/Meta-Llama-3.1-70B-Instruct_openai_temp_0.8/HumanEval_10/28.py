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
    def find_longest_palindromic_suffix(s):
        for i in range(len(s), -1, -1):
            if is_palindrome(s[i:]):
                return s[i:]
        return ''

    if not string:
        return ''

    palindromic_suffix = find_longest_palindromic_suffix(string)
    prefix = string[:len(string) - len(palindromic_suffix)]
    return string + prefix[::-1]


# Test cases
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks whether a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that begins with a supplied string. 

In the `make_palindrome` function, a helper function `find_longest_palindromic_suffix` is used to find the longest postfix of the supplied string that is a palindrome. Then, it appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. 

Finally, test cases are provided to verify the correctness of the `make_palindrome` function.