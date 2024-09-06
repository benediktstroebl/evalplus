```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    postfix = ''.join(char for char in string if char == string[0] else char for char in string)
    return postfix + string[1:].reverse() + postfix
```