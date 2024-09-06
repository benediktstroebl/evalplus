```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:0:-1] + string[::-1]
    return palindrome

def test_palindrome():
    assert is_palindrome("")
    assert is_palindrome("CAT")
    assert is_palindrome("cata")
    assert is_palindrome("preserved") == "preserved"
    assert is_palindrome("hello") == "olleh"
    assert is_palindrome("") == ""
```
The code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome constructs a palindrome given a string. The test_palindrome function verifies the correctness of the is_palindrome and make_palindrome functions by testing various inputs.