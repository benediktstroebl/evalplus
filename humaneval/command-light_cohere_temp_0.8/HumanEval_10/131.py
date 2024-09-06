```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string.

    if not string: 
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    while string[-1] not int(): 
        string = string[:-len(string)-1] + string[-1:]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[::-1][::-1]
```