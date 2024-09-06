```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    palindrome = ""
    while True:
        # find the longest palindrome or fix-length prefix
        fixed_len = 0
        for j in range(1,len(string)):
            if string[j] == string[-(j+1)] and j < fixed_len:
                fixed_len = j
        palindrome += string[:fixed_len] + string[-fixed_len:]
        break

    return palindrome
```