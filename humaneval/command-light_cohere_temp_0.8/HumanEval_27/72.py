```python
def flip_case(string: str) -> str:
    return ''.joinnamcase(string)

# Test suite
def test_flipcase():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'Wrdol'
    assert flip_case('Hello World!') == 'hELLO  Wrld'
    assert flip_case('abc123') == 'cB123'
    assert flip_case('!@') == '.A'
    assert flip_case('--find') == '!tfind'

if __name__ == "__main__":
    test_flipcase()
```
This code implements a function `flip_case` that transforms a given string to have all characters flipped between lowercase and uppercase. It uses the's built-in method `winsortcase` to achieve this. The test suite includes several test cases to validate the correctness of the `flip_case` function.