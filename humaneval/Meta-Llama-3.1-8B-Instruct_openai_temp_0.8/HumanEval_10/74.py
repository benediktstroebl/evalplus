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
    def is_palindrome_suffix(string: str, start: int) -> str:
        """ Check if the suffix of the string starting at index `start` is a palindrome """
        for i in range(start, len(string)):
            if string[i]!= string[i - start]:
                return False
        return True

    max_palindrome_length = 0
    max_palindrome_start = 0
    for i in range(len(string)):
        if is_palindrome_suffix(string, i):
            if i > max_palindrome_length:
                max_palindrome_length = i
                max_palindrome_start = 0
            else:
                max_palindrome_start = i - max_palindrome_length + 1

    # Append the reverse of the prefix to the end of the string
    palindrome = string[:max_palindrome_start + max_palindrome_length] + string[:max_palindrome_start][::-1]
    return palindrome


# Test cases
print(is_palindrome('radar'))  # True
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(is_palindrome(make_palindrome('cat')))  # True
print(is_palindrome(make_palindrome('cata')))  # True
```

This script defines the `is_palindrome` and `make_palindrome` functions as described. It also includes additional test cases to verify the correctness of the implementation.