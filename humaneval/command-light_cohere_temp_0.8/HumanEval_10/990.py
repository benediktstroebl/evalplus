```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    """
    if not string:
        return ''
    
    palindrome = string
    
    postfix = ''
    while True:
        is_palindrome = True
        left, right = 0, len(string) - 1
        while left <= right:
            char = string[left]
            right -= 1
            if char != postfix[::-1]:
                is_palindrome = False
                break
            postfix += char
        if is_palindrome:
            break
        
        palindrome += postfix
        postfix = ''
        
    return palindrome
```