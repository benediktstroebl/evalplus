```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ''
    palindrome = ''
    while True: 
        prefix = string[:len(string)-1] + string[-1:]
        if is_palindrome(prefix): 
            palindrome = prefix + palindrome[:-reverse(palindrome)]
            break
        else: 
            palindrome = prefix + palindrome[:reverse(palindrome)]
    return palindrome
``` 
The `is_palindrome` function checks if the given string is a palindrome, and the `make_palindrome` function constructs the shortest palindrome using the algorithm provided.