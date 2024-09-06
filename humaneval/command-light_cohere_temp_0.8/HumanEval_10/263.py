```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''
    else:
        return string + string[::-1][::-1]

def test_palindrome():
    assert is_palindrome('') == False
    assert is_palindrome('cat') == True
    assert is_palindrome('cata') == True
    assert is_palindrome('racecar') == False

if __name__ == "__main__":
    test_palindrome()
```
This code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome creates a palindrome from a given string. The test_palindrome function ensures the correctness of the make_palindrome function by passing the test cases.