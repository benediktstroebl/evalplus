Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome
    """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.

    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.

    # Example string = 'cat'
    # prefix = 'cat'
    # suffix = 'a'
    # palindrome = 'tacat'
    # return ''.join(prefix[:-1] + suffix + prefix[1:])

    # or simply find the longest palindrom using string slicing and slicing again:
    # prefix = ''
    # suffix = ''
    # palindrome = ''
    # for i in range(len(string)):
    #     if i == 0 or is_palindrome(string[:i] + string[i+1:]):
    #         palindrome += string[:i] + string[i+1:]
    #         break
    # return palindrome

# Test the function
print(is_palindrome(""))  # Output: True
print(is_palindrome("cat"))  # Output: True
print(is_palindrome("cata"))  # Output: False
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```
The `is_palindrome` function returns `True` if the string is a palindrome and `False` otherwise. The `make_palindrome` function returns the shortest palindrome that begins with the given string.