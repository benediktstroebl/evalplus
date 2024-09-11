### Solution
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
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
    if not string:
        return ""
    
    # Find the longest postfix that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            break
    
    # Reverse the prefix
    prefix = string[:i][::-1]
    
    # Append to the end of the string
    return string + prefix


# Test the function
if __name__ == "__main__":
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # 'catac'
    print(make_palindrome("cata"))  # 'catac'
```

### Explanation
The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the input string. It first checks if the input string is empty, in which case it returns an empty string. Otherwise, it finds the longest postfix of the string that is a palindrome by iterating from the end of the string. Once it finds the longest palindrome postfix, it reverses the prefix of the string (before the palindromic suffix) and appends it to the end of the string, resulting in a palindrome.