```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    ALGORITH: Find the longest postfix of supplied string that is a palindrome
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Test: simple and straightforward.
    """
   
    shortest palindrome of 'test' is 'est'.
    """

# Unit tests
test_make_palindrome = make_palindrome
assert test_make_palindrome('test') == 'est'

assert test_make_palindrome('') == ''

assert test_make_palindrome('cat') == 'catac'

assert test_make_palindrome('cata') == 'catac'

assert not_palindrome('test') == 'est'

assert not_palindrome('') == ''

assert not_palindrome('cat') == 'acat'

```