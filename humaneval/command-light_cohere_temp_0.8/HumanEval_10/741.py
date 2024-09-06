```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    # Find the longest postfix of supplied string that is a palindrome
    palindrome_len = 0
    palindrome = ""
    while True:
        palindrome_len = len(palindrome) + 1
        if palindrome_len == 1:
            break
        if palindrome[palindrome_len - 1] == palindrome[0]:
            palindrome = palindrome[::-1]
        else:
            palindrome = palindrome[0] + palindrome[palindrome_len - 1]
    return palindrome
```