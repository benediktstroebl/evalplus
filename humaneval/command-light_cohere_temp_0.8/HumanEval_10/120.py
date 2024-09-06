```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea: Find the longest palindrome prefix
    # and then append the reverse of it to the end.
    # Create a max length for the palindrome prefix
    palindrome_len = len(''.join("".join(string)))

    # Find the longest palindrome prefix
    palindrome = ''.join(string[:palindrome_len])

    # Append the reverse of the palindrome prefix
    # to the original string
    return string + palindrome[::-1]

def test_make_palindrome():
    assert make_palindrome('') == '', "Failed to create an empty palindrome"
    assert make_palindrome('cat') == 'catac', "Failed to create 'cat'"
    assert make_palindrome('cata') == 'catac', "Failed to create 'cata'"

if __name__ == "__main__":
    test_make_palindrome()
```
The function `make_palindrome` returns the shortest palindrome that begins with the supplied string. The function uses a algorithm idea to find the longest palindrome prefix and then append the reverse of it to the end of the original string.