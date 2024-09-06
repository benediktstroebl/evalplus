```python
def is_palindrome(string: str) -> bool:
    """ Check if given string is a palindrome or not """  
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Create a palindrome from a given string """  
    if not string:
        return ''

    palindrome_start = 0
    while palindrome_start < len(string) - 1:
        is_palindrome_char = string[palindrome_start] == string[palindrome_start + 1]
        if is_palindrome_char:
            palindrome_end = palindrome_start + 1
            palindrome = string[palindrome_start:palindrome_end] + string[palindrome_end:palindrome_start]
            palindrome_start = palindrome_end + 1
        else:
            palindrome_start += 1

    return palindrome
```