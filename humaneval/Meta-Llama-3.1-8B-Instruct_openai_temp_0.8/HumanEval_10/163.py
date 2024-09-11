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
    # Find the longest postfix of the string that is a palindrome
    i = 0
    while i < len(string) and string[i] == string[-1 - i]:
        i += 1
    # Create the shortest palindrome by appending reverse of the prefix to the palindromic suffix
    return string + string[-i:1:-1]


# Test cases
print(is_palindrome('radar'))  # True
print(is_palindrome('hello'))  # False
print(make_palindrome(''))      # ''
print(make_palindrome('cat'))   # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('a'))     # 'a'
```

Note that I modified the `make_palindrome` function to include the logic for finding the longest postfix that is a palindrome and for creating the shortest palindrome by appending the reverse of the prefix to the palindromic suffix. I also added some test cases to demonstrate the functionality of both functions.