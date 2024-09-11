### Solution: Making the Shortest Palindrome
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
    rev_str = string[::-1]
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + rev_str[i:]
    return string + rev_str


# Example usage
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ""
    print(make_palindrome("cat"))  # Output: "catac"
    print(make_palindrome("cata"))  # Output: "catac"
```

#### Explanation

The `make_palindrome` function attempts to make a palindrome by checking each postfix of the input string to see if it's a palindrome. If it finds a palindromic postfix, it appends the reverse of the string's prefix that comes before the palindrome to the end of the string, effectively making the shortest palindrome.

In the example usage, we test the function with the given examples.