```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'fail'

    palindrome = string[:0:len(string)//2]
    return palindrome

def test():
    assert is_palindrome(''), "It should be a palindrome"
    assert is_palindrome('racecar')
    assert is_palindrome('hello')
    assert is_palindrome('world')

# Call the function to test
test()
```