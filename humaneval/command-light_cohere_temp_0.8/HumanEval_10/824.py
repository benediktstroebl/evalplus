Here is a self-contained Python function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    if not is_palindrome(string):
        return ''  # No palindrome found

    # Find the longest postfix of supplied string that is a palindrome
    palindrome_end = string[:len(string) // 2] + palindrome_start
    return palindrome_end + string[::-1]
```
This function is designed to determine if a given string is a palindrome, and if not, it returns an empty string. It uses a`is _palindrome()` function to test if the string is a palindrome, and if not, returns `None`. It then checks if `None` was returned, which means there is no palindrome. If the function did return, it proceeds to find the longest postfix of the supplied string that is a palindrome. It does this by creating a palindrome_end string, which is the longest palindrome prefix. It then appends the either the palindrome_start or the original string, and then appends it to the reverse of the palindrome_start.