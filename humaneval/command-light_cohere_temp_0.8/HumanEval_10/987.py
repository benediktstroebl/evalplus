```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''
    
    palindrome = ''
    while True:
        is_palindrome = True
        for i in range(1, len(string)):
            if string[i] != string[len(string) - i]:
                is_palindrome = False
                break
        if is_palindrome:
            break
        palindrome += string[::-1]

    return palindrome
```