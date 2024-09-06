```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''
    
    palindrome = []
    while True:
        palindrome.append(char)
        if char == palindrome[::-1]:
            char = '+' + char
            break
        else:
            palindrome.append(char)
    
    return ''.join(palindrome)

# Unit tests
def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

# Main Function Call
test_make_palindrome()
```
This script defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` generates the shortest palindrome given a string. 

The `make_palindrome` function uses a simple algorithm to create the palindrome. 

The test_make_palindrome function then verifies the output of the `make_palindrome` function for various input strings.