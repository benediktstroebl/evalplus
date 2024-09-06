```python
def flip_case(string):
    return ''.join_case(string.lower() if string.isalpha('lower') else ''.upper() else ''.lower())

def test_flip_case():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('HEllO') == 'olleH'
    assert flip_case('ABC defini') == 'DefiABC'
    assert flip_case('hello world') == 'dlrow ohLLO w'
    assert flip_case(' Oswald') != 'osWALD'
```
This Python code defines a function `flip_case` that converts a given string into a title case version. It also includes a test_flip_case, a function that asserts the correctness of the `flip_case` function.