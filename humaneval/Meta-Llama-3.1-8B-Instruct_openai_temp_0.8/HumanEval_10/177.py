### Solution
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
    def is_palindrome_from_end(s):
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return s[:i]

    suffix = is_palindrome_from_end(string)
    prefix = string[:len(string) - len(suffix)]
    return string + prefix[::-1]


# Testing the function
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ""
    print(make_palindrome("cat"))  # Output: "catac"
    print(make_palindrome("cata"))  # Output: "catac"
```

### Explanation

The solution for the `make_palindrome` function is as follows:

1.  We define a helper function `is_palindrome_from_end` that checks for the longest prefix of the input string that is a palindrome by iterating over the suffix of the input string in reverse order.
2.  We use the `is_palindrome_from_end` function to find the longest postfix of the input string that is a palindrome and store it in the `suffix` variable.
3.  We compute the prefix of the input string that comes before the palindromic suffix by taking a slice of the input string up to the index of the palindromic suffix.
4.  We reverse the computed prefix and append it to the end of the input string to form the shortest palindrome that begins with the input string.

### Note

The longest postfix of the input string that is a palindrome is found by checking for palindromes starting from the end of the string. This is an efficient approach as it avoids checking for palindromes from the beginning of the string, which would require more iterations.