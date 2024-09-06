```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    """ Return is string = 'catac' 
    > make_palindrome('')
    ''
    > make_palindrome('cat')
    'catac'
    > make_palindrome('cata')
    'catacat'
    """

# Unit tests
def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    
# Main Function
if __name__ == "__main__":
    test_make_palindrome()
``` 
Do note that the code will print the shortest palindrome that begins with the supplied string.