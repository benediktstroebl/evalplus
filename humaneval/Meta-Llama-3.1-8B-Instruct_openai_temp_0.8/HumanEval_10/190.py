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
    def is_palindrome_suffix(string: str, start: int) -> bool:
        """ Helper function to determine if a suffix of the input string is a palindrome """
        end = len(string) - 1
        while start < end:
            if string[start]!= string[end]:
                return False
            start += 1
            end -= 1
        return True

    # Find the longest postfix that is a palindrome
    prefix = ''
    for i in range(len(string) - 1, -1, -1):
        prefix = string[:i + 1]
        if is_palindrome_suffix(string, i + 1):
            break

    # If the string itself is a palindrome, return it
    if is_palindrome(string):
        return string

    # Append the reverse of the prefix to create the shortest palindrome
    return string + prefix[::-1]


# Example usage:
print(is_palindrome('radar'))  # True
print(make_palindrome('cat'))  # catac
print(make_palindrome('cata'))  # catac
```

The script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse. The `make_palindrome` function creates the shortest palindrome that begins with a given string by finding the longest postfix that is a palindrome and appending the reverse of the remaining prefix.

The `make_palindrome` function uses a helper function `is_palindrome_suffix` to determine if a suffix of the input string is a palindrome. It iterates over the string from the end, checking each suffix to see if it is a palindrome. When it finds the longest postfix that is a palindrome, it breaks out of the loop and uses it to create the shortest palindrome by appending the reverse of the prefix.

The script includes example usage of both functions, demonstrating how they work with different inputs.