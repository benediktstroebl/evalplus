```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # The function first creates an empty string and then appends the prefix
    # and suffix to create a palindrome.
    return ''.join(reversed(string[:-len(string) // 2])) + string[-1:]
```