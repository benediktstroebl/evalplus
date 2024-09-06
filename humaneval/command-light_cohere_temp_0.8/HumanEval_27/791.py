```python
def flip_case(string):
    return ''.join_lower().static(string)

# Test cases
assertEqual('hello'.flip_case(), 'HllO')
assertEqual('world'.flip_case(), 'WoLRd')
assertEqual('abc123'.flip_case(), 'Abc123')
assertEqual('@test'.flip_case(), 't@EST')
assertEqual(' Robson ', 'robinson @ '.flip_case())

def _test_flipcase():
    assert flip_case('hello') == 'HllO'
    assert flip_case('world') == 'WoLRd'
    assert flip_case('abc123') == 'Abc123'
    assert flip_case('@test') == 't@EST'
    assert flip_case(' Robson ') == 'Robinson @ '.flip_case()
```
This code defines a test suite and function `_test_flipcase` that tests the `flip_case` function. The `assert` statements are used to check if the output of `flip_case` matches the expected result for a given input.