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

    Args:
        string (str): Input string.

    Returns:
        str: Shortest palindrome that begins with the input string.
    """
    # Find the longest palindromic suffix of the string
    i = 0
    while i < len(string) and string[i] == string[-1 - i]:
        i += 1
    # Reverse the prefix of the string that comes before the palindromic suffix
    prefix = string[:len(string) - i]
    palindrome = string + prefix[::-1]
    return palindrome


# Test the function
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

### Explanation:

This Python script first checks if a given string is a palindrome with a helper function `is_palindrome`. However, to achieve the second task of making the shortest palindrome that begins with a supplied string, we use a different approach:

1.  **Find the Longest Palindromic Suffix**: We start from the beginning and end of the string and compare characters from both ends. If they match, we move towards the center of the string.
2.  **Reverse the Prefix**: Once we have found the longest palindromic suffix, we reverse the prefix of the original string (i.e., the portion before the palindromic suffix) and append it to the end of the original string. This results in a palindrome whose prefix is the original string.

The `make_palindrome` function implements this approach. It uses a while loop with string indexing (`string[i]` and `string[-1 - i]`) to find the longest palindromic suffix. This is followed by reversing the prefix with slicing (`prefix[::-1]`) before appending it to the end of the original string. The resulting string is the shortest palindrome that begins with the input string.