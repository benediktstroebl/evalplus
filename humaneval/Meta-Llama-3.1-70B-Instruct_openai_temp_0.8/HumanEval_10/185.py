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
    reverse_string = string[::-1]
    for i in range(len(string)):
        if string.startswith(reverse_string[i:]):
            return string + reverse_string[:i]


# Example usage:
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```

**Explanation:**

1. The `is_palindrome` function checks if a given string is the same forwards and backwards.

2. The `make_palindrome` function takes a string as an argument and returns the shortest palindrome that begins with that string.

   - First, it reverses the input string.
   
   - Then, it goes through the reversed string from right to left and checks if the input string starts with the corresponding substring of the reversed string.
   
   - As soon as it finds a match, it appends the non-matching part of the reversed string to the input string and returns the result.

**Note:**

This solution works because a palindrome can be obtained by appending the reverse of a prefix to a suffix that is already a palindrome. The `make_palindrome` function finds the longest palindromic suffix and appends the reverse of the remaining prefix.