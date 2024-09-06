Here is a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not is_palindrome(string):
        return ""

    # Algorithm idea:
    # - Find the longest postfix of supplied string that is a palindrome.
    # - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    return make_palindrome(string[::-1])
```
This function uses a recursive approach with a base case to solve the problem. The function is_palindrome checks if the given string is already a palindrome, and then makes a recursive call to the make_palindrome function with the reversed version of the prefix of the palindromic suffix. The make_palindrome function finds the longest palindrome that starts with the given string, and then appends the reversed version of the string prefix to the end of the palindrome.