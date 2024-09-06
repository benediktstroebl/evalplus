```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = ''
    for char in string:
        if is_palindrome(char):
            longest_palindrome += char[::-1]
        else:
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return longest_palindrome + longest_palindrome[::-1]
```
The function is_palindrome checks if a given string is a palindrome, and the function make_palindrome uses this function to create the shortest palindrom starting with the input string.