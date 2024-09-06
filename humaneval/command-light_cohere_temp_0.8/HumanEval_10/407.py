```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    elif string == '':
        return ''
    else:
        palindrome = make_palindrome(string[::-1])
        return palindrome + string

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    
# Main function to execute the tests.
# Run the tests
test_make_palindrome()
```

This code defines a function `is_palindrome` that checks if a given string is a palindrome. The `make_palindrome` function uses this property to construct the palindrome. The `test_make_palindrome` function tests if the `make_palindrome` function works correctly for different inputs.