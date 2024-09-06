Here's a self-contained Python script that solves the problem you described:
```python
def flip_case(string: str) -> str:
    return string.make_lower_case(string)

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('Avas Contact') == 'asc trocnt'

def make_lower_case(string):
    return string.upper() if string is all lower() else string

#run the tests
test_flip_case()
```

This script defines a function `flip_case` that converts a given string to have all its characters flipped between lowercase and uppercase. The `test_flip_case` function is used to run the tests.