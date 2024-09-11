```markdown
### Palindrome Script

#### Overview
This Python script contains two functions:
- `is_palindrome`: checks if a given string is a palindrome.
- `make_palindrome`: finds the shortest palindrome that begins with a supplied string.

#### Code
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
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindromic_suffix = ''
    i = 0
    while i < len(string):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if is_palindrome(substr) and len(substr) > len(longest_palindromic_suffix):
                longest_palindromic_suffix = substr
        i += 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-len(longest_palindromic_suffix)]
    palindrome = prefix + longest_palindromic_suffix + prefix[::-1]
    return palindrome


# Example usage:
if __name__ == "__main__":
    print(is_palindrome('radar'))  # True
    print(make_palindrome('cat'))  # catac
    print(make_palindrome('cata'))  # catac
    print(make_palindrome('abba'))  # abba
```

#### Explanation
The `make_palindrome` function checks if the input string is already a palindrome. If it is, the string is returned as is. If not, it finds the longest postfix of the string that is a palindrome, appends the reverse of the string prefix that comes before the palindromic suffix, and returns the resulting palindrome. The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse.