This Python script defines a function that checks if a given string is a palindrome, and another function to generate a palindrome given a prefix. 

```python
def is_palindrome(string):
    """ Tests if a given string is a palindrome. """
    return string == string[::-1] 

def make_palindrome(prefix):
    """ Generates the shortest palindrome that begins with a supplied string prefix. """ 
    if prefix == '': 
        return ''
    palindrome = prefix + prefix[::-1]
    return palindrome
```