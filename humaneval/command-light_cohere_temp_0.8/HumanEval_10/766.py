```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns: time complexity of O(n) where n is the length of the string."""
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string
    else:
        palindrome_start = 0
        palindrome_end = len(string) - 1
        while palindrome_start <= palindrome_end:
            is_palindrome = True
            for i in range(0, len(string) - 1):
                if string[i] != string[i + 1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                palindrome_start = i + 1
                break
        palindrome_end -= 1
        return string[:palindrome_start] + string[-palindrome_end + 1:]
```