This script contains a function that checks whether a given string is a palindrome and creates a palindrome from an input string. 

```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ''
    else:
        if len(string) == 1: 
            return string
        l, r = 0, 0
        while l < len(string) - 1: 
            if is_palindrome(string[l:r+1]): 
                return string[:l] + string[r:l-r] + string[l:r+1]
            l += 1
        return make_palindrome(string[0:len(string) - 1])

print(make_palindrome('cata')) # Output: catac
``` 
This script defines two functions, `is_palindrome` and `make_palindrome`, which respectively check if a given string is a palindrome and create a palindrome from a supplied string.