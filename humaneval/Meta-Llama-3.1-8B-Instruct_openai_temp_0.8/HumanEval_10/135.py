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
    if not string:
        return ''

    i = 0
    while i < len(string):
        # check for palindrome from the end
        palindromic_suffix = ''
        j = i
        while j < len(string):
            if string[j] == string[i]:
                palindromic_suffix += string[j]
                j += 1
                i += 1
            else:
                break
        
        # if palindromic suffix is found, proceed to make palindrome
        if i!= len(string):
            return string + string[:len(string) - i][::-1]

        i += 1


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `is_palindrome` function, the `make_palindrome` function, and includes test cases for the `make_palindrome` function. The `make_palindrome` function uses a while loop to find the longest palindromic suffix from the end of the string, then appends the reverse of the string prefix to the end to form the shortest palindrome. If no palindromic suffix is found, it returns the original input string.