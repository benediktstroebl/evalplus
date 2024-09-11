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
    if not string:  # if input string is empty
        return string

    # find the longest palindromic postfix
    for i in range(len(string), 0, -1):
        postfix = string[-i:]  # take i characters from the end of the string
        if is_palindrome(postfix):
            break  # we've found the longest palindromic postfix

    # append the reverse of the prefix to the end of the string
    prefix = string[:-i]  # all chars before the palindromic postfix
    palindrome = string + prefix[::-1]

    return palindrome


# Test cases
print(make_palindrome(""))  # ''
print(make_palindrome("cat"))  # catac
print(make_palindrome("cata"))  # catac
```
This script defines the `make_palindrome` function which takes a string as input, finds the longest palindromic postfix, and appends the reverse of the prefix before it to the end of the string to form the shortest palindrome. The `is_palindrome` function is used as a helper function to check if a given string is a palindrome. The script also includes test cases to verify the correctness of the `make_palindrome` function.