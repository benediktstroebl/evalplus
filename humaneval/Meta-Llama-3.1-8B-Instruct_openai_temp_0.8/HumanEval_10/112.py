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
    # Find the longest postfix that's a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            # Reverse the prefix and append
            prefix = string[:-i]
            return postfix + prefix[::-1]

    # If no palindromic postfix is found, return the original string
    return string


# Test cases
if __name__ == "__main__":
    print(is_palindrome("radar"))  # True
    print(is_palindrome("python"))  # False
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # 'catac'
    print(make_palindrome("cata"))  # 'catac'
```

This script first checks if the input string is a palindrome using the `is_palindrome` function. It then uses the `make_palindrome` function to find the shortest palindrome that begins with the input string. The `make_palindrome` function works by finding the longest postfix of the input string that is a palindrome, reversing the prefix that comes before it, and appending it to the postfix. If no palindromic postfix is found, the function returns the original string.