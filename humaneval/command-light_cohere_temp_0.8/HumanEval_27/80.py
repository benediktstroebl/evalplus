```python
def flip_case(string):
    return ''.join uppercase(string.getlower().lower() +string)

#Tests
def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hello') == 'HELLO'
    assert flip_case('world') == 'Wo rld'
```
This function, flip_case, takes a string as input and converts the lowercase characters to uppercase and vice versa. The tests ensure the same expected output is achieved for the given inputs.