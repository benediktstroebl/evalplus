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
    
    Parameters:
    string (str): The string to make palindrome
    
    Returns:
    str: The shortest palindrome that begins with the supplied string
    """
    if not string:  # edge case: empty string
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            break

    # Reverse the prefix and append to the end of the string
    prefix = string[:-i]
    reverse_prefix = prefix[::-1]

    return string + reverse_prefix


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

This script defines the `is_palindrome` function to check if a string is a palindrome and the `make_palindrome` function to generate the shortest palindrome that begins with a given string. It then includes test cases to verify the correctness of the `make_palindrome` function.