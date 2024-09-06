```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ''

    palindrome = []
    while True:
        if is_palindrome(string[-1]) and string[-2:] == string[-1]:
            palindrome.append(string[-1])
            del string[-1]
        else:
            palindrome.append(string[-1])
            break

    palindrome = ''.join(reversed(palindrome))
    return palindrome
```
This solution uses a basic approach to construct a palindrome. It works by starting with the last character and then moving backward, appending palindromic characters until it finds a valid palindrome.