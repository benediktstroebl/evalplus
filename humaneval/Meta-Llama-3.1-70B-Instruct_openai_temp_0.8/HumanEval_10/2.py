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
    str: The shortest palindrome that begins with the input string.
    """
    if not string:  # if the string is empty, return it as it is
        return string

    for i in range(len(string), 0, -1):  # iterate from the end of the string to the beginning
        postfix = string[i:]  # get the postfix of the current length
        if is_palindrome(postfix):  # check if the postfix is a palindrome
            prefix = string[:i]  # get the prefix that comes before the palindromic suffix
            return string + prefix[::-1]  # append the reverse of the prefix to the end of the string

    # if no palindromic postfix is found, the string itself is the shortest palindrome
    return string + string[::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('abcddcba'))  # 'abcddcba'
print(make_palindrome('abba'))  # 'abba'
```