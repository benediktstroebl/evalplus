Here's the code with the above mentioned function:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = []
    for char in string:
        if char == palindrome[-1] or char == palindrome[0]:
            break
        else:
            palindrome.append(char)

    return ''.join(palindrome[::-1])
```
I hope this helps!