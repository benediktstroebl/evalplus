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
    while palindrome[-1] not in 'cat----------':
        palindrome = palindrome[:-len(palindrome) - 1] + palindrome
    return palindrome
 ```

The code defines a Python function `is_palindrome` that tests if a given string is a palindrome, and another function `make_palindrome` that constructs the shortest palindrome using the idea of concatenating a prefix that is a palindrome and the reverse of the suffix.