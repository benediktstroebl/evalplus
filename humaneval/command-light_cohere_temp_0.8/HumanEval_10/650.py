```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ''
    # Find the longest postfix of supplied string that is a palindrome.
    postfix = []
    palindrome = ''
    for char in string:
        if char == palindrome[::-1]:
            postfix.append(char)
        else:
            postfix.append(char)
            palindrome = char
    return palindrome[::-1]+postfix[::-1]
```
The function is_palindrome checks if the given string is a palindrome or not. The function make_palindrome creates a palindrome by finding the longest palindromic postfix and then appends it to the original string.