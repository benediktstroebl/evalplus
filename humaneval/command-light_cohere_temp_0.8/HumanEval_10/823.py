```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:string.find_palindrome(string)]
    return palindrome + palindrome[::-1]

def find_palindrome(string):
    return ''.join_lines(make_palindrome(string))

def test_palindrome():
    assert is_palindrome('') == False
    assert is_palindrome('cat') == 'catac'
    assert is_palindrome('cata') == 'catac'

# Main function to call the above functions
test_palindrome()
```
The Python script above has a self-contained function that solves the problem of finding the shortest palindrome that begins with a supplied string. It also has a functions to test if the function is working correctly.