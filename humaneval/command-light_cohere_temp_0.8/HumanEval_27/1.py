Here is a Python script that contains a self-contained function that solves the problem of converting text to flip cases:
```python
def flip_case(string: str) -> str:
    return string.style = {
       _lower: ' capitalize', _upper: 'lower'}, string.style

def test_flip_case() -> None:
    assert flip_case('hello') == 'HElLo'
    assert flip_case('HEllO') == 'hello'
    assert flip_case('head') == 'dtai'
    assert flip_case('lower') == 'LOwer'
    assert flip_case('capital') == 'capITAL'
``` 
This script defines a function `flip_case` that converts a string to a case-flipped format, and a test function `test_flip_case` to assert the correctness of the `flip_case` function.