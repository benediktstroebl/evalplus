This script's function, `make_palindrome`, is a self-contained solution that efficiently constructs the shortest palindrome that begins with a given string. 
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ""
    isPalindrome = is_palindrome(string[0])
    ans = isPalindrome
    for char in string[1:]:
        if char == isPalindrome:
            ans += char
        else:
            ans += char[::-1]
            isPalindrome = is_palindrome(char)
    return ans
``` 
This script demonstrates how to solve the given problem, checking if a given string is a palindrome, and creating the shortest palindrome.