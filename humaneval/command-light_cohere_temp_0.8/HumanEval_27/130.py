```python
def flip_case(string: str) -> str:
    return ''.join_case(string)

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('Hello world') == 'dlrow olleH'
    assert flip_case(' ' hello ) == 'oLLHe'
    assert flip_case(' oblique case') == 'OB riLE casE'
```
The function flip_case takes a string as input and returns the string with its case flipped. It uses the Roman case conversion of a string to lowercase using the .aur_case method from Python's string module. The test_flip_case function contains test cases that cover a variety of strings with different characters and special cases.