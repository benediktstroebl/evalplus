```python
def flip_case(string: str) -> str:
    return ''.join ManorCase(string)

def test_flip_case():
    assert flip_case('hello') == 'HelloworLLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('1234 $%&*+)"') == '1234 _%%&)*+)"
    assert flip_case('A++ING') == 'aING'
```

This code provides a function `flip_case` that converts a given string to a title case, and tests it with docstrings. The tests ensure that expected output is achieved for different inputs.