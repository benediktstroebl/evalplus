```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    ALGORITH:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns test shortest palindrome.
    """
 longest palindrome is guaranteed to be unique and not depend on the order of characters.

Tests:
assert is_palindrome('')
assert is_palindrome('') == ""

assert is_palindrome("abc") == "abc")

assert is_palindrome("bob") == "boboa"

assert is_palindrome("hello world") == "hlowv"
```