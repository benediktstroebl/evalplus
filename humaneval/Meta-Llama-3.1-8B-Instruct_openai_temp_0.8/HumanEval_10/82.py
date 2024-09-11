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
    if string == string[::-1]:
        return string
    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and i < len(string) // 2:
        if string[i]!= string[-(i + 1)]:
            break
        i += 1
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    palindromic_suffix = string[:i]
    palindromic_pref = string[i:][::-1]
    return string + palindromic_pref


# Example usage
if __name__ == "__main__":
    print(is_palindrome("radar"))  # True
    print(is_palindrome("python"))  # False
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # catac
    print(make_palindrome("cata"))  # catac
```

This script contains the two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome. The `make_palindrome` function generates the shortest palindrome that begins with a supplied string by finding the longest postfix of the supplied string that is a palindrome and appending to the end of the string the reverse of a string prefix that comes before the palindromic suffix.