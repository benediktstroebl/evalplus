```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string
    while True:
        if palindrome[-1:] == palindrome[1:]:
            palindrome = palindrome[:-len(palindrome)-2]
        else:
            break
    
    # Append to the string reverse of a string prefix that comes before the palindromic suffix
    return palindrome + palindrome[::-1]
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` creates the shortest palindrome that begins with a given string. The `make_palindrome` function uses a simple algorithm to find the longest palindrom in the string, and then appends the reverse of a palindromic prefix to the string.