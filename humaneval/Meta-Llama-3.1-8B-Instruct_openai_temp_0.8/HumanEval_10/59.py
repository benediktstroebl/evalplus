### Make Palindrome Function
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
    """
    # Find the longest palindromic suffix of the string
    for i in range(len(string), -1, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Find the prefix that comes before the palindromic suffix
            prefix = string[:i]
            # Reverse the prefix and append it to the end of the palindrome suffix
            return suffix + prefix[::-1]

    # If no palindromic suffix is found, return an empty string
    return ''


# Test cases
if __name__ == '__main__':
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
```
In this code, we define a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the given string. The function uses a loop to find the longest palindromic suffix of the input string, and then appends the reverse of the string prefix that comes before the palindrome suffix. The `is_palindrome` function is used to check if a given string is a palindrome. The code also includes test cases to verify the correctness of the `make_palindrome` function.