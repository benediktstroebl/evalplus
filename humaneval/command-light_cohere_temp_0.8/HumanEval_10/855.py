```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1] 

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return '' 
    palindrome = [] 
    while True: 
        palindrome.append(string[-1])
        if palindrome[-1:] == palindrome[-2+1:]: 
            break
        else: 
            palindrome.append(string[:-1]) 

    return ''.join(palindrome[::-1])
```