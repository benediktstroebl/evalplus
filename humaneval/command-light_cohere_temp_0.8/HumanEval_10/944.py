```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join_palindrome(string)
    return ''.join_palindrome(string)[::-1]

def join_palindromes(string):
    return ''.join_palindrome(string)

def _test_palindromes():
    assert is_palindrome('')
    assert is_palindrome('cat')
    assert is_palindrome('cata')
    assert join_palindromes('') == 'catac'
    assert join_palindromes('coba') == 'acot'
    assert join_palindromes('agat') == 'gatca'

if __name__ == "__main__":
    _test_palindromes()
```
The code defines a set of functions related to checking and creating palindromes, which includes the main test suite. The function is_palindrome checks if a given string is a palindrome. The function make_palindrome creates the shortest palindrome that starts with the given string. The function join_palindromes joins a series of palindromes together. The _test_palindromes function contains unit tests to check the correctness of the is_palindrome and make_palindrome functions.