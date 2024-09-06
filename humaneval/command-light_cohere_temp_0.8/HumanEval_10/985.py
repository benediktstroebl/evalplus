```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ""
    
    palindrome = string[:0:-1] + string[::-1]
    return palindrome

def test_make_palindrome():
    assert make_palindrome("") == "", " Palindrome not found for empty string"
    assert make_palindrome("cat") == "catac", " Palindrome doesn't work!"
    assert make_palindrome("cata") == "catac", " Palindrome doesn't work!"
```
The `make_palindrome` function creates the longest palindrome using a similar approach and passes the test cases.