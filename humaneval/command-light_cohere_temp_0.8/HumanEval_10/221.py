```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea: Find the longest postfix of the string that is a palindrome
    # then append the reverse of the prefix to the end of the string
    palindrome_part = string[:0:-1]  # string prefix that is a palindrome
    return palindrome_part + string[::-1]

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

if __name__ == "__main__":
    print("Testing make_palindrome function:")
    test_make_palindrome()
```
The `make_palindrome` function determines whether a given string can be a palindrome and returns it if it can. The `is_palindrome` function determines whether a given string is a palindrome and returns `True` if it is and `False` otherwise. The `test_make_palindrome` function asserts that the `make_palindrome` function produces the expected results for certain inputs.