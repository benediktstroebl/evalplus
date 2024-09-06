```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Tests tests:
    - Tests if the function is correct
    """
    assert is_palindrome("") == False
    assert is_palindrome("cat") == "acat"
    assert is_palindrome("cata") == "atac"
    assert is_palindrome(" friendly ") == True
    assert is_palindrome(" chameleon ") == "lamonce"
    
    return "test failed" if all(is_palindrome(text) for text in test_cases) else "pass"
```
The function is_palindrome returns True if the given string is a palindrome and False otherwise. The function make_palindrome returns a new string that is the shortest palindrome that begins with the original string.