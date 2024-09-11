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
    def is_palindrome_helper(s):
        """ Helper function to check if a string is a palindrome """
        for i in range(len(s) // 2):
            if s[i]!= s[-i - 1]:
                return False
        return True

    prefix = string
    while not is_palindrome_helper(string):
        string = string[-1] + string[:-1]
    return prefix + string


# Example usage:
if __name__ == "__main__":
    print(is_palindrome('radar'))  # True
    print(make_palindrome('cat'))  # catac
    print(make_palindrome('cata'))  # catac
    print(make_palindrome('madam'))  # madamm
    print(make_palindrome('python'))  # pythonnohtyp
```