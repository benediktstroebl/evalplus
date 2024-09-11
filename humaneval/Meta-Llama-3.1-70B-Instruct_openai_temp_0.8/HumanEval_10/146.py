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
        str: Shortest palindrome string that begins with the input string.
    """
    if not string:  # if string is empty, return it immediately
        return string

    for i in range(len(string), 0, -1):  # iterate over all possible postfix lengths
        postfix = string[-i:]  # get the last 'i' characters of the string
        if is_palindrome(postfix):  # if the postfix is a palindrome
            prefix = string[:-i]  # get the prefix that comes before the palindromic suffix
            return string + prefix[::-1]  # return the shortest palindrome string


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abba'))  # 'abba'
print(make_palindrome('abc'))  # 'abcba'
```