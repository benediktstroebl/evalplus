```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ""
    else:
        # Find the longest postfix of supplied string that is a palindrome
        postfix = ""
        for c in string:
            if c == postfix[-1]:
                postfix += c
            else:
                break
        postfix = postfix[::-1]

        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        return string + postfix
```