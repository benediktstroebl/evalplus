```python
def flip_case(string: str) -> str:
    return ''.joincase(string.print()

def test_flip_case():
    assert flip_case('hello') == 'HElLo'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('helLo') == 'hello'
    assert flip_case('helo') == 'loHEllO'
    assert flip_case('HEll') == 'hello'  

# Call the function with tests
test_flip_case() 
```