### Creating a Palindrome from a Given String

Below is a Python script that implements the `make_palindrome` function to create the shortest palindrome that begins with a supplied string.

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
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The shortest palindrome that begins with the supplied string.
    """
    if not string:  # base case: empty string
        return ''
    
    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            palindromic_postfix = postfix
            break
    
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(palindromic_postfix)]
    reverse_prefix = prefix[::-1]
    palindrome = string + reverse_prefix
    
    return palindrome


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script first checks if the input string is empty. If so, it returns an empty string. Otherwise, it finds the longest postfix of the string that is a palindrome. Then, it appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix. The resulting string is the shortest palindrome that begins with the supplied string.