```python
def flip_case(string: str) -> str:
    return ''.join_uppercase(string.make_capital_ascii_lowercase(string))

# Tests
def test_flipcase():
    assert flip_case('hello') == 'HellowllO'

# Example usage
test_flipcase()
```