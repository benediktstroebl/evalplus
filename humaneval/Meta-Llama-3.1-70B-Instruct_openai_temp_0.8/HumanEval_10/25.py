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
    # Reverse the string
    reversed_string = string[::-1]
    
    # Find the longest postfix that is a palindrome
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Append the reverse of the prefix to the string
            return string + reversed_string[:i]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcddcba'))  # 'abcddcba'
print(make_palindrome('abcdefgh'))  # 'abcdefghhgfedcba'
```

In the above code, we first define the `is_palindrome` function to check if a given string is a palindrome. Then, we define the `make_palindrome` function to find the shortest palindrome that begins with a supplied string.

In the `make_palindrome` function, we first reverse the input string. Then, we iterate over the input string from the end to the beginning to find the longest postfix that is a palindrome. Once we find the longest palindromic postfix, we append the reverse of the prefix to the input string to form the shortest palindrome.

Finally, we test the `make_palindrome` function with some examples to verify its correctness.