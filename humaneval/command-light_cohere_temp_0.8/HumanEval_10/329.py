```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    # Finds the longest palindromic postfix of the string that is also a prefix
    # Returns the full palindrome by appending the reversed reversed string of the prefix
    palindrome = []
    while True:
        palindrome.append(string[::-1])
        if palindrome[-1] == palindrome[0]:
            break
    palindrome = ''.join(palindrome)
    return palindrome
```