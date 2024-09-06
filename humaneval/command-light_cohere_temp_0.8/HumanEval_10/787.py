```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ''

    palindrome = string
    
    while True:
        l = len(palindrome)
        l1 = 0
        for i in range(1, l):
            if palindrome[i] == palindrome[l-i]:
                l1 = i
                break
        else:
            palindrome = palindrome[l:] + palindrome[l1:]
            break

    return palindrome
```