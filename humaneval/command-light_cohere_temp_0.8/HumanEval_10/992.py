```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join_palindrome(string)
    return string + _palindrome(string[::-1])

def _palindrome(sub):
    if sub == sub[::-1]:
        return sub
    return _palindrome(sub[1:]) + sub[0]

def __tests__():
    assert is_palindrome('') == False
    assert is_palindrome('cat') == True
    assert is_palindrome('cata') == True
    assert is_palindrome('racecar') == False
    assert is_palindrome('words') == False
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('racecar') == 'racecar'
    assert make_palindrome('words') == 'wordsw'
    assert _palindrome('racecar') == 'racecar'
    assert _palindrome('cata') == 'atacata'
    assert _palindrome('') == ''
```